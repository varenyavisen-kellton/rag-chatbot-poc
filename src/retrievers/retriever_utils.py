from langchain_core.documents import Document


def chroma_result_to_documents(result):

    documents = []

    for doc, metadata in zip(
        result["documents"],
        result["metadatas"]
    ):
        documents.append(
            Document(
                page_content=doc,
                metadata=metadata
            )
        )

    return documents