import os
import pathlib
import sys

# Support running tests directly or via pytest
try:
    from src.gemini_client import GeminiClient
except ImportError:
    project_root = pathlib.Path(__file__).resolve().parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from src.gemini_client import GeminiClient


def test_mock_mode_response_structure(monkeypatch):
    monkeypatch.setenv("GEMINI_MOCK", "1")
    client = GeminiClient()
    out = client.analyze(system_prompt="x", user_prompt="y")
    assert isinstance(out, dict)
    assert "steps" in out
    assert isinstance(out["steps"], list)


if __name__ == "__main__":
    # Basic test without pytest fixtures
    os.environ["GEMINI_MOCK"] = "1"
    client = GeminiClient()
    out = client.analyze(system_prompt="x", user_prompt="y")
    assert isinstance(out, dict)
    assert "steps" in out
    assert isinstance(out["steps"], list)
    print("✓ test_mock_mode_response_structure passed")


