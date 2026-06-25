# src/retrievers/hybrid_retriever.py

import re

from src.vectorstore.chroma_manager import (
    get_chroma_collection
)

from src.retrievers.root_cause_retriever import (
    retrieve_root_cause
)

from src.retrievers.transaction_retriever import (
    search_transactions
)

from src.retrievers.error_retriever import (
    search_errors
)

from src.retrievers.incident_retriever import (
    search_incidents
)

from src.retrievers.lead_retriever import (
    search_leads
)

from langchain_core.documents import Document


# -------------------------
# REGEX HELPERS
# -------------------------

def extract_transaction_id(query):

    pattern = (
        r"[a-f0-9]{8}-"
        r"[a-f0-9]{4}-"
        r"[a-f0-9]{4}-"
        r"[a-f0-9]{4}-"
        r"[a-f0-9]{12}"
    )

    match = re.search(
        pattern,
        query.lower()
    )

    if match:
        return match.group()

    return None


def extract_lead_id(query):

    pattern = r"LD\d+"

    match = re.search(
        pattern,
        query,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return None


def extract_incident_id(query):

    pattern = r"INC\d+"

    match = re.search(
        pattern,
        query,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return None


# -------------------------
# METADATA LOOKUPS
# -------------------------

def lookup_transaction(transaction_id):

    collection = get_chroma_collection(
        "transactions"
    )
    result = collection.get(
    where={
        "transaction_id": transaction_id
    }
)

    return convert_get_result_to_documents(
    result
)



def lookup_lead(lead_id):

    collection = get_chroma_collection(
        "leads"
    )
    result = collection.get(
    where={
        "lead_id": lead_id
    }
)

    return convert_get_result_to_documents(
    result
)


# -------------------------
# MAIN ROUTER
# -------------------------

def retrieve(query):

    transaction_id = extract_transaction_id(
        query
    )

    transaction_id = extract_transaction_id(
    query
)

    if transaction_id:

        print(
            "\nUsing Root Cause Retrieval\n"
        )

        return retrieve_root_cause(
            transaction_id
        )

    lead_id = extract_lead_id(
        query
    )

    if lead_id:

        print(
            "\nUsing Lead Metadata Retrieval\n"
        )

        return lookup_lead(
            lead_id
        )

    query_lower = query.lower()

    # -------------------------
    # ERROR ROUTING
    # -------------------------

    error_keywords = [
        "error",
        "failure",
        "failed",
        "timeout",
        "gateway",
        "critical",
        "exception"
    ]

    if any(
        keyword in query_lower
        for keyword in error_keywords
    ):

        print(
            "\nUsing Error Retrieval\n"
        )

        return search_errors(
            query,
            k=5
        )

    # -------------------------
    # INCIDENT ROUTING
    # -------------------------

    incident_keywords = [
        "incident",
        "outage",
        "downtime",
        "root cause"
    ]

    if any(
        keyword in query_lower
        for keyword in incident_keywords
    ):

        print(
            "\nUsing Incident Retrieval\n"
        )

        return search_incidents(
            query,
            k=5
        )

    # -------------------------
    # LEAD ROUTING
    # -------------------------

    lead_keywords = [
        "loan",
        "application",
        "customer",
        "lead"
    ]

    if any(
        keyword in query_lower
        for keyword in lead_keywords
    ):

        print(
            "\nUsing Lead Retrieval\n"
        )

        return search_leads(
            query,
            k=5
        )

    # -------------------------
    # DEFAULT
    # -------------------------

    print(
        "\nUsing Transaction Retrieval\n"
    )

    return search_transactions(
        query,
        k=5
    )


def convert_get_result_to_documents(
    result
):

    documents = []

    docs = result.get(
        "documents",
        []
    )

    metas = result.get(
        "metadatas",
        []
    )

    for doc, meta in zip(
        docs,
        metas
    ):

        documents.append(
            Document(
                page_content=doc,
                metadata=meta
            )
        )

    return documents