import os

from src.gemini_client import GeminiClient


def test_mock_mode_response_structure(monkeypatch):
    monkeypatch.setenv("GEMINI_MOCK", "1")
    client = GeminiClient()
    out = client.analyze(system_prompt="x", user_prompt="y")
    assert isinstance(out, dict)
    assert "steps" in out
    assert isinstance(out["steps"], list)


