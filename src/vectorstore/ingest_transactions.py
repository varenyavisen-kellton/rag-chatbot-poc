import pandas as pd

from src.processing.transaction_documents import (
    create_transaction_document
)

from src.vectorstore.ingestion_utils import (
    ingest_dataframe
)


def main():

    df = pd.read_csv(
        "data/raw/api_transaction_fact.csv"
    )

    ingest_dataframe(
        df=df,
        collection_name="transactions",
        document_builder=create_transaction_document,
        batch_size=1000
    )


if __name__ == "__main__":
    main()