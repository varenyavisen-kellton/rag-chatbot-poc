import pandas as pd

def clean_value(value):
    if pd.isna(value):
        return "Not Available"
    return str(value)