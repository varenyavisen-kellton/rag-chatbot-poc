from src.rag.rag_chain import (
    ask_question
)

question = (
    "Why did transaction "
    "a65e6416-f7ec-4614-802c-0d5ebeb2cb32 fail?"
)

response = ask_question(question)

print("\nQUESTION\n")
print(question)

print("\nANSWER\n")
print(response)