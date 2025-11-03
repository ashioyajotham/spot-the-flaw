## Setup Instructions

1. Install Python 3.9+ and create a virtual environment.
2. `pip install -r requirements.txt`
3. Copy `env.example` to `.env` and set `GEMINI_API_KEY`.
4. Optionally set `GEMINI_MODEL_NAME` or enable `GEMINI_MOCK=1` for offline.
5. Run UI: `streamlit run src/ui/app.py` or CLI: `python src/main.py --proof path.json`.

