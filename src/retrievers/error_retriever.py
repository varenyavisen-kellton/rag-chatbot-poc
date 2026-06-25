# src/retrievers/error_retriever.py

from src.vectorstore.chroma_manager import (
    get_chroma_collection
)


def search_errors(query, k=5):

    collection = get_chroma_collection(
        "errors"
    )

    results = collection.similarity_search(
        query,
        k=k
    )

    return results