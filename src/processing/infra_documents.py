from langchain_core.documents import Document
from src.processing.utils import clean_value


def create_infra_document(row):

    content = f"""
Metric Timestamp: {clean_value(row['metric_timestamp'])}
Host Name: {clean_value(row['host_name'])}
CPU Usage: {clean_value(row['cpu_usage'])}
Memory Usage: {clean_value(row['memory_usage'])}
Disk Usage: {clean_value(row['disk_usage'])}
Active Threads: {clean_value(row['active_threads'])}
Request Count: {clean_value(row['request_count'])}
Error Count: {clean_value(row['error_count'])}
"""

    metadata = {
        "host_name": clean_value(row["host_name"]),
        "metric_timestamp": clean_value(row["metric_timestamp"])
    }

    return Document(
        page_content=content,
        metadata=metadata
    )