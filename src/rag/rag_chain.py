from langchain_ollama import OllamaLLM

from src.retrievers.hybrid_retriever import retrieve

from src.rag.context_builder import (
    build_context
)

from src.rag.prompt import (
    RAG_PROMPT
)


llm = OllamaLLM(
    model="mistral"
)


def ask_question(question):

    docs = retrieve(question)

    context = build_context(
        docs
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(
        prompt
    )

    return response