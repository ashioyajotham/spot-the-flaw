import pathlib
import sys

# Support running tests directly or via pytest
try:
    from src.proof_analyzer import analyze_proof
except ImportError:
    project_root = pathlib.Path(__file__).resolve().parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from src.proof_analyzer import analyze_proof


def test_analyze_proof_mock(monkeypatch):
    monkeypatch.setenv("GEMINI_MOCK", "1")
    payload = {"proof_id": "t1", "steps": [{"step_number": 1, "content": "x"}]}
    out = analyze_proof(payload)
    assert out["overall_status"] in {"correct", "contains_errors", "unknown"}


if __name__ == "__main__":
    # Basic test without pytest fixtures
    import os
    os.environ["GEMINI_MOCK"] = "1"
    payload = {"proof_id": "t1", "steps": [{"step_number": 1, "content": "x"}]}
    out = analyze_proof(payload)
    assert out["overall_status"] in {"correct", "contains_errors", "unknown"}
    print("✓ test_analyze_proof_mock passed")

