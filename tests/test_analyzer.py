from src.proof_analyzer import analyze_proof


def test_analyze_proof_mock(monkeypatch):
    monkeypatch.setenv("GEMINI_MOCK", "1")
    payload = {"proof_id": "t1", "steps": [{"step_number": 1, "content": "x"}]}
    out = analyze_proof(payload)
    assert out["overall_status"] in {"correct", "contains_errors", "unknown"}

