import pandas as pd

from src.processing.infra_documents import (
    create_infra_document
)

from src.vectorstore.ingestion_utils import (
    ingest_dataframe
)


def main():

    df = pd.read_csv(
        "data/raw/infra_metric_fact.csv"
    )

    ingest_dataframe(
        df=df,
        collection_name="infra",
        document_builder=create_infra_document,
        batch_size=1000
    )


if __name__ == "__main__":
    main()