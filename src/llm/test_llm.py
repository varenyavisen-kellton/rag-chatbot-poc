from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

response = llm.invoke(
    "Explain Retrieval Augmented Generation in 3 lines."
)

print(response)