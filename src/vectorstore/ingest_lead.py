import pandas as pd

from src.processing.lead_documents import (
    create_lead_document
)

from src.vectorstore.ingestion_utils import (
    ingest_dataframe
)


def main():

    df = pd.read_csv(
        "data/raw/lead_master.csv"
    )

    ingest_dataframe(
        df=df,
        collection_name="leads",
        document_builder=create_lead_document,
        batch_size=1000
    )


if __name__ == "__main__":
    main()