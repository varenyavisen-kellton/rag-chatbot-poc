from langchain_core.documents import Document
from src.processing.utils import clean_value


def create_lead_document(row):

    content = f"""
Lead ID: {clean_value(row['lead_id'])}
Customer ID: {clean_value(row['customer_id'])}
Application ID: {clean_value(row['application_id'])}
Created Timestamp: {clean_value(row['created_timestamp'])}
Source Channel: {clean_value(row['source_channel'])}
Product Type: {clean_value(row['product_type'])}
Loan Amount: {clean_value(row['loan_amount'])}
Current Status: {clean_value(row['current_status'])}
"""

    metadata = {
        "lead_id": clean_value(row["lead_id"]),
        "customer_id": clean_value(row["customer_id"]),
        "application_id": clean_value(row["application_id"]),
        "current_status": clean_value(row["current_status"])
    }

    return Document(
        page_content=content,
        metadata=metadata
    )