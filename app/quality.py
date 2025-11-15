def generate_quality_report(raw_len: int, cleaned_df):
    return {
        "rows_received": raw_len,
        "rows_cleaned": len(cleaned_df),
        "invalid_rows": raw_len - len(cleaned_df),
        "missing_values": cleaned_df.isna().sum().to_dict()
    }
