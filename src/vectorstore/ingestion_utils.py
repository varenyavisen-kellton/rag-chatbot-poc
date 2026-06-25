# src/vectorstore/ingestion_utils.py

from tqdm import tqdm
from src.vectorstore.chroma_manager import get_chroma_collection


def ingest_dataframe(
    df,
    collection_name,
    document_builder,
    batch_size=1000
):
    """
    Convert dataframe rows into documents
    and store them in ChromaDB in batches.
    """

    collection = get_chroma_collection(
        collection_name
    )

    total_rows = len(df)

    print(
        f"\nIngesting {total_rows} rows into "
        f"'{collection_name}' collection"
    )

    for start_idx in tqdm(
        range(0, total_rows, batch_size)
    ):

        end_idx = min(
            start_idx + batch_size,
            total_rows
        )

        batch_df = df.iloc[start_idx:end_idx]

        documents = []

        for _, row in batch_df.iterrows():
            documents.append(
                document_builder(row)
            )

        collection.add_documents(
            documents
        )

    print(
        f"\nCompleted ingestion for "
        f"{collection_name}"
    )