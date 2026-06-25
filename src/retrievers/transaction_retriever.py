# src/retrievers/transaction_retriever.py

from src.vectorstore.chroma_manager import (
    get_chroma_collection
)


def search_transactions(query, k=5):

    collection = get_chroma_collection(
        "transactions"
    )

    results = collection.similarity_search(
        query,
        k=k
    )

    return results