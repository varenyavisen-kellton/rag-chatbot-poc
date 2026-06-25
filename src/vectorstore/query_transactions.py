from src.vectorstore.chroma_manager import get_chroma_collection


def main():

    collection = get_chroma_collection(
        "transactions"
    )

    results = collection.similarity_search(
        "transaction timeout failure",
        k=5
    )

    print("\nTOP RESULTS\n")

    for i, doc in enumerate(results, start=1):

        print(f"\n===== RESULT {i} =====")
        print(doc.page_content[:500])
        print(doc.metadata)


if __name__ == "__main__":
    main()