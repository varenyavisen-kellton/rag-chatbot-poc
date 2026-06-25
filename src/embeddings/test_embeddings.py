from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = """
Transaction failed because vendor API timed out.
"""

embedding = embedding_model.embed_query(text)

print(f"Vector Length: {len(embedding)}")
print(embedding[:5])