import pandas as pd

from transaction_documents import create_transaction_document
from error_documents import create_error_document
from incident_documents import create_incident_document
from infra_documents import create_infra_document
from lead_documents import create_lead_document


def build_documents(df, document_builder):
    """
    Convert dataframe rows into LangChain Documents.
    """
    documents = []

    for _, row in df.iterrows():
        documents.append(document_builder(row))

    return documents


def main():

    print("Loading datasets...\n")

    transactions_df = pd.read_csv(
        "data/raw/api_transaction_fact.csv"
    )

    errors_df = pd.read_csv(
        "data/raw/application_error_fact.csv"
    )

    incidents_df = pd.read_csv(
        "data/raw/incident_master.csv"
    )

    infra_df = pd.read_csv(
        "data/raw/infra_metric_fact.csv"
    )

    leads_df = pd.read_csv(
        "data/raw/lead_master.csv"
    )

    print("Building transaction documents...")
    transaction_docs = build_documents(
        transactions_df,
        create_transaction_document
    )

    print("Building error documents...")
    error_docs = build_documents(
        errors_df,
        create_error_document
    )

    print("Building incident documents...")
    incident_docs = build_documents(
        incidents_df,
        create_incident_document
    )

    print("Building infra documents...")
    infra_docs = build_documents(
        infra_df,
        create_infra_document
    )

    print("Building lead documents...")
    lead_docs = build_documents(
        leads_df,
        create_lead_document
    )

    print("\n===== DOCUMENT COUNTS =====")

    print(f"Transactions : {len(transaction_docs)}")
    print(f"Errors       : {len(error_docs)}")
    print(f"Incidents    : {len(incident_docs)}")
    print(f"Infra        : {len(infra_docs)}")
    print(f"Leads        : {len(lead_docs)}")

    total_docs = (
        len(transaction_docs)
        + len(error_docs)
        + len(incident_docs)
        + len(infra_docs)
        + len(lead_docs)
    )

    print(f"\nTotal Documents: {total_docs}")


if __name__ == "__main__":
    main()