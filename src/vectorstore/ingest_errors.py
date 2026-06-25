import pandas as pd

from src.processing.error_documents import (
    create_error_document
)

from src.vectorstore.ingestion_utils import (
    ingest_dataframe
)


def main():

    df = pd.read_csv(
        "data/raw/application_error_fact.csv"
    )

    ingest_dataframe(
        df=df,
        collection_name="errors",
        document_builder=create_error_document,
        batch_size=1000
    )


if __name__ == "__main__":
    main()