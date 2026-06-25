from langchain_core.documents import Document
import pandas as pd
from src.processing.utils import clean_value


def create_transaction_document(row):

    content = f"""
Transaction ID: {clean_value(row['transaction_id'])}
Lead ID: {clean_value(row['lead_id'])}
API Name: {clean_value(row['api_name'])}
Vendor: {clean_value(row['vendor_name'])}
HTTP Status: {clean_value(row['http_status'])}
Latency: {clean_value(row['latency_ms'])} ms
Success Flag: {clean_value(row['success_flag'])}
Error Code: {clean_value(row['error_code'])}
Error Message: {clean_value(row['error_message'])}
Request Timestamp: {clean_value(row['request_timestamp'])}
Response Timestamp: {clean_value(row['response_timestamp'])}
"""

    metadata = {
    "transaction_id": clean_value(row["transaction_id"]),
    "lead_id": clean_value(row["lead_id"]),
    "trace_id": clean_value(row["trace_id"]),
    "vendor_name": clean_value(row["vendor_name"]),
    "success_flag": clean_value(row["success_flag"]),
    "api_name": clean_value(row["api_name"]),
    "http_status": str(row["http_status"])
    }

    return Document(
        page_content=content,
        metadata=metadata
    )