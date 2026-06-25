from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def get_chroma_collection(collection_name):

    return Chroma(
        collection_name=collection_name,
        embedding_function=embedding_model,
        persist_directory="chroma_db"
    )