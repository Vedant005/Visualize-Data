import pandas as pd
import numpy as np
from src.utils.storage import load_dataset

class BasicAutoService:
    def __init__(self):
        pass

    def generate_basic_visuals(self, dataset_id: str):
        df = load_dataset(dataset_id)

        if df is None or df.empty:
            raise ValueError("Dataset is empty or not found")

        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

        visuals = []
        # histogram
        for col in numeric_cols:
            series = pd.to_numeric(df[col], errors="coerce").dropna()
            if series.empty:
                continue

            counts, edges = np.histogram(series, bins=20)

            visuals.append({
                "type": "histogram",
                "column": col,
                "counts": counts.tolist(),
                "edges": edges.tolist()
            })
    
       # Bar chart
        for col in categorical_cols:
            vc = df[col].value_counts().head(15)

            visuals.append({
                "type": "bar",
                "column": col,
                "x": vc.index.tolist(),
                "y": vc.values.tolist()
            })

        # Box plot
        for col in numeric_cols:
            series = pd.to_numeric(df[col], errors="coerce").dropna()
            if series.empty:
                continue

            visuals.append({
                "type": "boxplot",
                "column": col,
                "stats": {
                    "min": float(series.min()),
                    "q1": float(series.quantile(0.25)),
                    "median": float(series.median()),
                    "q3": float(series.quantile(0.75)),
                    "max": float(series.max())
                }
            })

       
        #  Coorelation matrix
        
        if len(numeric_cols) >= 2:
            corr = df[numeric_cols].corr().round(3).fillna(0)
            visuals.append({
                "type": "correlation_matrix",
                "matrix": corr.to_dict()
            })

        return {
            "dataset_id": dataset_id,
            "basic_visualizations": visuals
        }
