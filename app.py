import os
import streamlit as st

from ingest import create_vector_database
from rag import ask_question
from config import UPLOAD_FOLDER

st.set_page_config(
    page_title="RAG AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("🤖 RAG AI Chatbot")
st.write("Upload one or more PDF documents and ask questions from them.")

with st.sidebar:

    st.header("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("📤 Upload PDF"):

            save_path = os.path.join(
                UPLOAD_FOLDER,
                uploaded_file.name
            )

            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            with st.spinner("Updating knowledge base..."):
                create_vector_database()

            st.success("✅ Knowledge base updated successfully!")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question about your PDFs...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):
        answer = ask_question(question)

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )