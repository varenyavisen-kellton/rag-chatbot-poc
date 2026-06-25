# src/retrievers/incident_retriever.py

from src.vectorstore.chroma_manager import (
    get_chroma_collection
)


def search_incidents(query, k=5):

    collection = get_chroma_collection(
        "incidents"
    )

    results = collection.similarity_search(
        query,
        k=k
    )

    return results
