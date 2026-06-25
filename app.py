import streamlit as st

from src.rag.rag_chain import ask_question


# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Birla AI Assistant",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Birla AI Operations Assistant")


# ----------------------------
# CHAT HISTORY
# ----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ----------------------------
# DISPLAY HISTORY
# ----------------------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )


# ----------------------------
# CHAT INPUT
# ----------------------------

question = st.chat_input(
    "Ask about transactions, incidents, leads, errors..."
)


if question:

    # Display user message

    with st.chat_message(
        "user"
    ):
        st.markdown(
            question
        )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Generate answer

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Thinking..."
        ):

            answer = ask_question(
                question
            )

        st.markdown(
            answer
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )