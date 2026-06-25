# src/retrievers/root_cause_retriever.py

from src.vectorstore.chroma_manager import (
    get_chroma_collection
)

from langchain_core.documents import (
    Document
)

def get_root_cause_context(
    transaction_id
):

    collection = get_chroma_collection(
        "transactions"
    )

    result = collection.get(
        where={
            "transaction_id": transaction_id
        }
    )

    if not result["documents"]:
        return None

    return {
        "document":
            result["documents"][0],

        "metadata":
            result["metadatas"][0]
    }

def get_errors_by_trace_id(
    trace_id
):

    collection = get_chroma_collection(
        "errors"
    )

    result = collection.get(
        where={
            "trace_id": trace_id
        }
    )

    documents = []

    for doc, meta in zip(
        result["documents"],
        result["metadatas"]
    ):

        documents.append(
            Document(
                page_content=doc,
                metadata=meta
            )
        )

    return documents

def get_lead(
    lead_id
):

    collection = get_chroma_collection(
        "leads"
    )

    result = collection.get(
        where={
            "lead_id": lead_id
        }
    )

    documents = []

    for doc, meta in zip(
        result["documents"],
        result["metadatas"]
    ):

        documents.append(
            Document(
                page_content=doc,
                metadata=meta
            )
        )

    return documents


def retrieve_root_cause(
    transaction_id
):

    transaction = get_root_cause_context(
        transaction_id
    )

    if transaction is None:
        return []

    metadata = transaction[
        "metadata"
    ]

    trace_id = metadata[
        "trace_id"
    ]

    lead_id = metadata[
        "lead_id"
    ]

    docs = []

    docs.append(
        Document(
            page_content=transaction[
                "document"
            ],
            metadata=metadata
        )
    )

    docs.extend(
        get_errors_by_trace_id(
            trace_id
        )
    )

    docs.extend(
        get_lead(
            lead_id
        )
    )

    return docs