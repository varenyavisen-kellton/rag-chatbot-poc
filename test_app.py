# app_test.py

import streamlit as st

from langchain_ollama import OllamaLLM

st.title("LLM Test")

if st.button("Run"):

    llm = OllamaLLM(
        model="mistral"
    )

    response = llm.invoke(
        "Say hello"
    )

    st.write(response)