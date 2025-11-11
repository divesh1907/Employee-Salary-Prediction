from typing import List
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def build_preprocessor(df: pd.DataFrame, target: str) -> ColumnTransformer:
    features = df.drop(columns=[target])
    num_cols = features.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = [c for c in features.columns if c not in num_cols]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols),
        ]
    )
    return preprocessor
