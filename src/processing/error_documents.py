from langchain_core.documents import Document
from src.processing.utils import clean_value
import pandas as pd


def create_error_document(row):
    """
    Convert a row from application_error_fact.csv
    into a LangChain Document.
    """

    content = f"""
Timestamp: {clean_value(row['timestamp'])}
Lead ID: {clean_value(row['lead_id'])}
Service Name: {clean_value(row['service_name'])}
API Name: {clean_value(row['api_name'])}
Severity: {clean_value(row['severity'])}
Error Code: {clean_value(row['error_code'])}
Error Message: {clean_value(row['error_message'])}
Trace ID: {clean_value(row['trace_id'])}
"""

    metadata = {
        "lead_id": clean_value(row["lead_id"]),
        "trace_id": clean_value(row["trace_id"]),
        "severity": clean_value(row["severity"]),
        "service_name": clean_value(row["service_name"]),
        "api_name": clean_value(row["api_name"]),
        "error_code": clean_value(row["error_code"])
    }

    return Document(
        page_content=content,
        metadata=metadata
    )
