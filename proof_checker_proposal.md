# 🔍 Spot the Flaw: ML Math Proof Checker

An interactive demonstration showcasing Gemini 2.5 Pro's mathematical reasoning capabilities through probabilistic learning and machine learning proof verification.

## 📋 Project Overview

This demo presents mathematical proofs from ML/probability theory with intentionally injected errors. Gemini 2.5 Pro analyzes each proof step-by-step, identifies flaws, and provides corrected versions with detailed reasoning commentary.

## 🎯 Key Features

- **Visual Proof Analysis**: Step-by-step color-coded verification (correct/questionable/error)
- **ML-Focused Mathematics**: Proofs from probabilistic learning, information theory, and optimization
- **Real-time Reasoning**: Watch Gemini 2.5 Pro's thought process unfold
- **Interactive Interface**: Submit custom proofs or select from curated examples
- **Comparative View**: Side-by-side display of flawed vs. corrected proofs

## 🧮 Example Proof Topics

- Bias-Variance Decomposition
- Convergence of Gradient Descent
- Jensen's Inequality Applications
- Maximum Likelihood Estimation Properties
- Information Theory Bounds
- Probabilistic PAC Learning Guarantees

## 🏗️ Project Structure

```
proof-checker-demo/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── main.py                    # Main application entry
│   ├── gemini_client.py           # Gemini API integration
│   ├── proof_analyzer.py          # Proof parsing and analysis logic
│   └── ui/
│       ├── app.py                 # Streamlit/Gradio UI
│       └── components.py          # Reusable UI components
├── data/
│   ├── sample_proofs/
│   │   ├── flawed/               # Proofs with intentional errors
│   │   │   ├── bias_variance.json
│   │   │   ├── gradient_descent.json
│   │   │   └── jensen_inequality.json
│   │   └── correct/              # Reference correct proofs
│   └── prompts/
│       ├── system_prompt.txt     # Gemini system instructions
│       └── analysis_template.txt # Proof analysis prompt template
├── tests/
│   ├── test_analyzer.py
│   └── test_gemini_client.py
├── notebooks/
│   └── demo_exploration.ipynb    # Development and testing notebook
└── docs/
    ├── workshop_guide.md         # Facilitator guide
    └── setup_instructions.md     # Installation and configuration

```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Gemini API key (get from Google AI Studio)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/proof-checker-demo.git
cd proof-checker-demo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### Run the Demo

```bash
# Launch the interactive UI
streamlit run src/ui/app.py

# Or run CLI version
python src/main.py --proof data/sample_proofs/flawed/bias_variance.json
```

## 📦 Dependencies

```
google-generativeai>=0.3.0
streamlit>=1.28.0
python-dotenv>=1.0.0
pydantic>=2.0.0
rich>=13.0.0
pytest>=7.4.0
```

## 🎨 Demo Flow

1. **Select Proof**: Choose from ML/probability proofs or input custom proof
2. **Inject Errors** (optional): System can inject random errors for demo purposes
3. **Analyze**: Gemini 2.5 Pro examines each step
4. **Visualize**: Color-coded results with reasoning commentary
5. **Compare**: View original, flawed, and corrected versions side-by-side
6. **Export**: Save analysis results for later reference

## 🔧 Configuration

Edit `data/prompts/system_prompt.txt` to customize Gemini's analysis behavior:
- Verbosity level
- Focus areas (logical flow, notation, computational steps)
- Output format preferences

## 📊 Sample Output Structure

```json
{
  "proof_id": "bias_variance_001",
  "overall_status": "contains_errors",
  "steps": [
    {
      "step_number": 1,
      "content": "E[(y - f̂(x))²] = E[y²] - E[f̂(x)²]",
      "status": "error",
      "issue": "Missing cross term in expectation expansion",
      "correction": "E[(y - f̂(x))²] = E[y²] - 2E[yf̂(x)] + E[f̂(x)²]",
      "reasoning": "The expansion of (a-b)² requires all three terms..."
    }
  ],
  "summary": "Proof contains 1 critical error in step 1...",
  "corrected_proof": "..."
}
```

## 🎓 Workshop Usage

For workshop facilitators:
1. Start with a simple flawed proof to demonstrate capabilities
2. Progress to more subtle errors
3. Allow audience to suggest where errors might be
4. Reveal Gemini's analysis
5. Discuss implications for AI-assisted mathematical reasoning

See `docs/workshop_guide.md` for detailed facilitation notes.

## 🤝 Contributing

Contributions welcome! Please focus on:
- Additional ML/probability proof examples
- UI/UX improvements
- Error injection patterns
- Analysis prompt refinements

## 📝 License

MIT License - feel free to use for educational purposes

## 🙏 Acknowledgments

- Built for "Math Reasoning with Gemini 2.5 Pro" workshop
- Powered by Google's Gemini 2.5 Pro API
- Inspired by mathematical pedagogy in ML education

---

**Workshop Contact**: [Your contact info]  
**Demo Video**: [Link to demo recording]  
**Slides**: [Link to presentation slides]