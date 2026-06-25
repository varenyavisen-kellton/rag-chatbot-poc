import pandas as pd


def load_csv(path):
    """
    Load a CSV file and return a DataFrame.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loaded {path}")
        print(f"Shape: {df.shape}")
        return df

    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None


if __name__ == "__main__":

    files = {
        "transactions": "data/raw/api_transaction_fact.csv",
        "errors": "data/raw/application_error_fact.csv",
        "incidents": "data/raw/incident_master.csv",
        "infra": "data/raw/infra_metric_fact.csv",
        "leads": "data/raw/lead_master.csv"
    }

    dataframes = {}

    for name, path in files.items():
        df = load_csv(path)

        dataframes[name] = df

        print(f"\n{name.upper()} COLUMNS")
        print(df.columns.tolist())

    print("\nLoaded all datasets successfully.")