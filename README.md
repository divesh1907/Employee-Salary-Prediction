# ESP Project

A production-ready repository scaffold for the ESP machine learning project with a Streamlit app.

## ✨ Highlights
- Clean Python package layout (`src/`)
- Reproducible environment (`requirements.txt`)
- One-click local app: `streamlit run app.py`
- CI with GitHub Actions (lint + tests)
- Tests with `pytest`
- Notebook archived under `notebooks/`

## 📦 Project Structure
```
esp-project/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
├── Makefile
├── pyproject.toml
├── .github/workflows/ci.yml
├── src/
│   ├── esp/
│   │   ├── __init__.py
│   │   ├── preprocessing.py
│   │   ├── models.py
│   │   ├── train.py
│   │   └── evaluate.py
├── tests/
│   └── test_sanity.py
└── notebooks/
    └── ESP project.ipynb
```

## 🚀 Quickstart
```bash
# 1) Create & activate a virtualenv (recommended)
python -m venv .venv && . .venv/bin/activate  # on Windows: .venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt

# 3) Run the app
streamlit run app.py
```

## 🧠 How it works
- Upload a CSV, pick the target column, choose a model (RF/SVM/KNN/MLP/LogReg/GB).
- We auto-build a preprocessing pipeline using `ColumnTransformer` (scale numeric, one-hot encode categoricals).
- We split train/test, train the model, and report Accuracy/Precision/Recall/F1.
- You can download the trained pipeline as a `.joblib` file.

## 🧪 Tests
Run tests locally:
```bash
pytest -q
```

## 🔁 CI
The GitHub Actions workflow in `.github/workflows/ci.yml` installs dependencies and runs tests on `push` and `pull_request`.

## 📄 License
MIT © 2025
