import os
from typing import Any, Dict, Optional

from dotenv import load_dotenv


class GeminiClient:
    """Thin wrapper around google-generativeai with a mock fallback.

    Environment variables:
      - GEMINI_API_KEY: required for real requests
      - GEMINI_MODEL_NAME: optional override
      - GEMINI_MOCK=1: use deterministic mock instead of network calls
    """

    def __init__(self, model_name: Optional[str] = None) -> None:
        load_dotenv()
        self._mock_mode = os.getenv("GEMINI_MOCK", "0") == "1"
        self._api_key = os.getenv("GEMINI_API_KEY")
        self._model_name = model_name or os.getenv("GEMINI_MODEL_NAME") or "gemini-1.5-pro"

        if not self._mock_mode:
            try:
                import google.generativeai as genai  # type: ignore
            except Exception as exc:  # pragma: no cover
                raise RuntimeError(
                    "google-generativeai is required for live mode. Install requirements and set GEMINI_MOCK=1 to run offline."
                ) from exc
            if not self._api_key:
                raise RuntimeError("GEMINI_API_KEY not set and GEMINI_MOCK is disabled.")
            genai.configure(api_key=self._api_key)
            self._genai = genai
            self._model = genai.GenerativeModel(self._model_name)
        else:
            self._genai = None
            self._model = None

    def analyze(self, system_prompt: str, user_prompt: str) -> Dict[str, Any]:
        """Send composed prompts and return parsed JSON dict.

        The analyzer upstream expects a JSON object. We attempt to parse it
        from the model response text. In mock mode, return a deterministic sample.
        """

        if self._mock_mode:
            return {
                "proof_id": "mock_proof",
                "overall_status": "contains_errors",
                "steps": [
                    {
                        "step_number": 1,
                        "content": "Mock step",
                        "status": "error",
                        "issue": "Demonstration error",
                        "correction": "Demonstration correction",
                        "reasoning": "Mock mode explanation",
                    }
                ],
                "summary": "Mock mode response.",
                "corrected_proof": "...",
            }

        # Live mode
        response = self._model.generate_content(
            [
                {"role": "system", "parts": [system_prompt]},
                {"role": "user", "parts": [user_prompt]},
            ]
        )
        text = getattr(response, "text", None) or getattr(response, "candidates", None)
        if hasattr(response, "text"):
            raw = response.text
        else:
            raw = str(response)

        # Try to extract a JSON object from the text
        obj = self._extract_json_object(raw)
        if obj is None:
            # Last resort: wrap as a simple structure
            return {
                "proof_id": "unknown",
                "overall_status": "unknown",
                "steps": [],
                "summary": raw[:4000],
                "corrected_proof": "",
            }
        return obj

    @staticmethod
    def _extract_json_object(text: str) -> Optional[Dict[str, Any]]:
        import json
        import re

        # Find the first top-level JSON object
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            # Attempt to match fenced code blocks with json
            fence = re.search(r"```json\s*(\{[\s\S]*?\})\s*```", text, re.IGNORECASE)
            if fence:
                try:
                    return json.loads(fence.group(1))
                except Exception:
                    return None
            return None
        snippet = text[start : end + 1]
        try:
            return json.loads(snippet)
        except Exception:
            return None


