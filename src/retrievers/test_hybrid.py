from src.retrievers.hybrid_retriever import retrieve

query = "why did transaction a65e6416-f7ec-4614-802c-0d5ebeb2cb32 fail"

result = retrieve(query)

print(result)