from __future__ import annotations

import json
import pathlib
from typing import Any, Dict

from .gemini_client import GeminiClient


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPTS_DIR = PROJECT_ROOT / "data" / "prompts"


def _read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def build_user_prompt(proof_payload: Dict[str, Any], template_text: str) -> str:
    # The template may include placeholders like {proof_json}
    proof_json = json.dumps(proof_payload, ensure_ascii=False, indent=2)
    return template_text.replace("{proof_json}", proof_json)


def analyze_proof(proof_payload: Dict[str, Any]) -> Dict[str, Any]:
    system_prompt = _read_text(PROMPTS_DIR / "system_prompt.txt")
    template_text = _read_text(PROMPTS_DIR / "analysis_template.txt")
    user_prompt = build_user_prompt(proof_payload, template_text)

    client = GeminiClient()
    result = client.analyze(system_prompt=system_prompt, user_prompt=user_prompt)
    return result


def load_json_file(path: str | pathlib.Path) -> Dict[str, Any]:
    p = pathlib.Path(path)
    return json.loads(p.read_text(encoding="utf-8"))


def save_json_file(payload: Dict[str, Any], path: str | pathlib.Path) -> None:
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


