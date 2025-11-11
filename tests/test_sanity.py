from pathlib import Path

def test_files_exist():
    required = [
        "app.py",
        "requirements.txt",
        "README.md",
        "src/esp/__init__.py",
        "src/esp/preprocessing.py",
        "src/esp/models.py",
        "src/esp/train.py",
        "src/esp/evaluate.py",
    ]
    for rel in required:
        assert Path(rel).exists(), f"Missing: {rel}"
