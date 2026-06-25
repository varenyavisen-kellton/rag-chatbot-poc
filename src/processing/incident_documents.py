from langchain_core.documents import Document
from src.processing.utils import clean_value


def create_incident_document(row):

    content = f"""
Incident ID: {clean_value(row['incident_id'])}
Title: {clean_value(row['title'])}
Severity: {clean_value(row['severity'])}
Status: {clean_value(row['status'])}
Root Cause: {clean_value(row['root_cause'])}
Start Time: {clean_value(row['start_time'])}
End Time: {clean_value(row['end_time'])}
"""

    metadata = {
        "incident_id": clean_value(row["incident_id"]),
        "severity": clean_value(row["severity"]),
        "status": clean_value(row["status"])
    }

    return Document(
        page_content=content,
        metadata=metadata
    )