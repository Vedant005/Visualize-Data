import pandas as pd
import numpy as np
from typing import Tuple

def preprocess_dataframe(df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:

    original_columns = df.columns.tolist()

    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
    )

    for col in df.columns:

        if df[col].dtype == object:
            df[col] = pd.to_numeric(df[col], errors="ignore")

        try:
            df[col] = pd.to_datetime(df[col], errors="ignore")
        except:
            pass

    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col].fillna(df[col].median(), inplace=True)

        elif df[col].dtype == "object":
            df[col].fillna(df[col].mode()[0], inplace=True)

        else:
            df[col].fillna(method="ffill", inplace=True)

    df.drop_duplicates(inplace=True)

    df = df.loc[:, df.isnull().mean() < 0.6]

    metadata = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "original_columns": original_columns,
    }

    return df, metadata
