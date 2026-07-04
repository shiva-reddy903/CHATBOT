import streamlit as st
from rag import ask_question

st.set_page_config(
    page_title="RAG AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG AI Chatbot")
st.write("Ask question from your uploaded PDF.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question about your PDF...")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):
        answer = ask_question(question)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )