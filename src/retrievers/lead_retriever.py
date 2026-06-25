# src/retrievers/lead_retriever.py

from src.vectorstore.chroma_manager import (
    get_chroma_collection
)


def search_leads(query, k=5):

    collection = get_chroma_collection(
        "leads"
    )

    results = collection.similarity_search(
        query,
        k=k
    )

    return results