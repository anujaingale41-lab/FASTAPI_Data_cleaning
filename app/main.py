from fastapi import FastAPI
import pandas as pd
import json
from typing import List
import os

from app.schemas import RawProduct
from app.cleaners import clean_sales_data
from app.quality import generate_quality_report

app = FastAPI(
    title="Data Validation & Cleaning API",
    description="A simple FastAPI service to validate and clean sales data.",
    version="1.0.0"
)


# ---------------------------------------------------------
# 1️. Clean user-submitted JSON
# ---------------------------------------------------------
@app.post("/clean_json")
def clean_json(records: List[RawProduct]):
    df_raw = pd.DataFrame([r.dict() for r in records])
    df_clean = clean_sales_data(df_raw)
    report = generate_quality_report(len(df_raw), df_clean)

    return {
        "cleaned_data": df_clean.to_dict(orient="records"),
        "quality_report": report
    }


# ---------------------------------------------------------
# 2️. Clean sample.json from /sample_data folder
# ---------------------------------------------------------
@app.get("/sample")
def clean_sample_json():
    """Reads sample_data/sample.json, cleans it, and returns results."""

    # Build correct path: project_root/sample_data/sample.json
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "sample_data", "sample.json")

    try:
        with open(file_path, "r") as f:
            sample_data = json.load(f)

        # Validate using Pydantic
        validated = [RawProduct(**record) for record in sample_data]

        df_raw = pd.DataFrame([v.dict() for v in validated])
        df_clean = clean_sales_data(df_raw)
        report = generate_quality_report(len(df_raw), df_clean)

        return {
            "cleaned_data": df_clean.to_dict(orient="records"),
            "quality_report": report
        }

    except FileNotFoundError:
        return {"error": "sample.json not found"}

    except json.JSONDecodeError:
        return {"error": "sample.json contains invalid JSON"}
