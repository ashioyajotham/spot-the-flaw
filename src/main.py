import argparse
from pathlib import Path
from typing import Any, Dict

from .proof_analyzer import analyze_proof, load_json_file, save_json_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze a proof JSON using Gemini")
    parser.add_argument("--proof", required=True, help="Path to input proof JSON")
    parser.add_argument(
        "--out", default="analysis_output.json", help="Path to write analysis JSON"
    )
    args = parser.parse_args()

    proof: Dict[str, Any] = load_json_file(args.proof)
    result = analyze_proof(proof)
    save_json_file(result, args.out)

    print(f"Analysis written to {Path(args.out).resolve()}")


if __name__ == "__main__":
    main()


