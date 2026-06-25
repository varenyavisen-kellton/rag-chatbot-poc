from src.retrievers.hybrid_retriever import (
    retrieve
)

from src.rag.context_builder import (
    build_context
)

query = "show gateway timeout failures"

docs = retrieve(query)

context = build_context(
    docs
)

print(context)