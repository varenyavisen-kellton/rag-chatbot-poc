from src.retrievers.root_cause_retriever import (
    retrieve_root_cause
)

docs = retrieve_root_cause(
    "a65e6416-f7ec-4614-802c-0d5ebeb2cb32"
)

for doc in docs:

    print(
        "\n===================="
    )

    print(
        doc.page_content
    )