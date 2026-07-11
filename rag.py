import os

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

from config import (
    VECTOR_DB_PATH,
    EMBEDDING_MODEL,
    LLM_MODEL,
    TOP_K
)

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

llm = OllamaLLM(
    model=LLM_MODEL
)


def ask_question(question):

    if question is None or question.strip() == "":
        return "Please enter a question."

    if not os.path.exists(VECTOR_DB_PATH):
        return "Vector database not found. Please upload a PDF and create the vector database."

    db = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )

    docs = db.max_marginal_relevance_search(
        question,
        k=TOP_K,
        fetch_k=20
    )

    if not docs:
        return "No relevant information found."

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    sources = list(
        set(
            doc.metadata.get("source", "Unknown")
            for doc in docs
        )
    )

    prompt = f"""
You are an intelligent RAG AI Assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply exactly:

"I couldn't find that information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    answer = llm.invoke(prompt)

    answer += "\n\n**Sources:**\n"

    for source in sources:
        answer += f"- {source}\n"

    return answer


if __name__ == "__main__":

    while True:

        question = input("Ask: ")

        if question.lower() == "exit":
            break

        print()
        print(ask_question(question))