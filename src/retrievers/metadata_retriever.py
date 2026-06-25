from src.vectorstore.chroma_manager import (
    get_chroma_collection
)

from src.retrievers.retriever_utils import (
    chroma_result_to_documents
)


def get_transaction_by_id(transaction_id):

    collection = get_chroma_collection(
        "transactions"
    )

    result = collection.get(
        where={
            "transaction_id": transaction_id
        }
    )

    return chroma_result_to_documents(
        result
    )