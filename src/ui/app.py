import json
import pathlib
from typing import Any, Dict, List

import streamlit as st

from ..proof_analyzer import analyze_proof, load_json_file


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2]
SAMPLES_DIR = PROJECT_ROOT / "data" / "sample_proofs"


def list_sample_paths() -> List[pathlib.Path]:
    flawed = (SAMPLES_DIR / "flawed").glob("*.json")
    correct = (SAMPLES_DIR / "correct").glob("*.json")
    paths = sorted(list(flawed)) + sorted(list(correct))
    return paths


def color_for_status(status: str) -> str:
    mapping = {
        "correct": "#16a34a",
        "questionable": "#d97706",
        "error": "#dc2626",
    }
    return mapping.get(status.lower(), "#64748b")


def render_steps(steps: List[Dict[str, Any]]) -> None:
    for step in steps:
        status = step.get("status", "unknown")
        bg = color_for_status(status)
        st.markdown(
            f"<div style='border-left: 8px solid {bg}; padding: 0.5rem 0.75rem; margin: 0.5rem 0;'>"
            f"<strong>Step {step.get('step_number','?')}</strong>: {step.get('content','')}<br/>"
            f"<em>Status</em>: {status}<br/>"
            f"<em>Issue</em>: {step.get('issue','')}<br/>"
            f"<em>Correction</em>: {step.get('correction','')}<br/>"
            f"<em>Reasoning</em>: {step.get('reasoning','')}"
            f"</div>",
            unsafe_allow_html=True,
        )


def main() -> None:
    st.set_page_config(page_title="Spot the Flaw: Proof Checker", layout="wide")
    st.title("🔍 Spot the Flaw: ML Math Proof Checker")
    st.caption("Analyze proofs, highlight issues, and view suggested corrections.")

    with st.sidebar:
        st.header("Input")
        samples = list_sample_paths()
        sample_labels = [p.relative_to(PROJECT_ROOT).as_posix() for p in samples]
        selected = st.selectbox("Choose a sample proof", [""] + sample_labels)
        uploaded = st.file_uploader("Or upload a proof JSON", type=["json"])
        run_btn = st.button("Analyze")

    proof: Dict[str, Any] | None = None
    if selected:
        proof = load_json_file(PROJECT_ROOT / selected)
    elif uploaded is not None:
        proof = json.loads(uploaded.read().decode("utf-8"))

    if run_btn:
        if proof is None:
            st.warning("Please select or upload a proof JSON.")
            return

        with st.spinner("Analyzing with Gemini..."):
            result = analyze_proof(proof)

        st.subheader("Overall Result")
        st.write({k: v for k, v in result.items() if k != "steps"})

        st.subheader("Step-by-step Analysis")
        render_steps(result.get("steps", []))

        st.subheader("Raw JSON")
        st.json(result)


if __name__ == "__main__":
    main()


