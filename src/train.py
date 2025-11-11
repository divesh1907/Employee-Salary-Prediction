from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from .preprocessing import build_preprocessor
from .models import get_model

def train_and_eval(df: pd.DataFrame, target: str, model_name: str, test_size: float = 0.2, random_state: int = 42):
    X = df.drop(columns=[target])
    y = df[target]

    pre = build_preprocessor(df, target)
    model = get_model(model_name)
    pipe = Pipeline([("pre", pre), ("model", model)])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y if y.nunique() > 1 else None)
    pipe.fit(X_train, y_train)

    y_pred = pipe.predict(X_test)
    metrics = dict(
        accuracy=accuracy_score(y_test, y_pred),
        precision=precision_score(y_test, y_pred, average="weighted", zero_division=0),
        recall=recall_score(y_test, y_pred, average="weighted", zero_division=0),
        f1=f1_score(y_test, y_pred, average="weighted", zero_division=0),
    )
    return pipe, metrics
