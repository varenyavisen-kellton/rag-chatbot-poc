def build_context(documents):

    context = ""

    for i, doc in enumerate(documents, start=1):

        context += (
            f"\n===== DOCUMENT {i} =====\n"
        )

        context += doc.page_content

        context += "\n"

    return context