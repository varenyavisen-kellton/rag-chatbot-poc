import pandas as pd

from src.processing.incident_documents import (
    create_incident_document
)

from src.vectorstore.ingestion_utils import (
    ingest_dataframe
)


def main():

    df = pd.read_csv(
        "data/raw/incident_master.csv"
    )

    ingest_dataframe(
        df=df,
        collection_name="incidents",
        document_builder=create_incident_document,
        batch_size=1000
    )


if __name__ == "__main__":
    main()