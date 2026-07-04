from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from config import(
    VECTOR_DB_PATH,
    EMBEDDING_MODEL
)
embeddings = HuggingFaceEmbeddings(
    model_name = EMBEDDING_MODEL
)
db = Chroma(
    persist_directory = VECTOR_DB_PATH,
    embedding_function = embeddings
)
llm = OllamaLLM(
    model = "llama3.2"
)
def ask_question(question):
    if question is None or question.strip()=="":
        return "Please enter a question"
    docs = db.similarity_search(question,k=3)
    print(docs)
    print(len(docs))
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"""
you are a helpful AI assistant.
Answer ONLY from the context below.
Context:
{context}
Question:
{question}
Answer:
"""
    response = llm.invoke(prompt)
    return response

if __name__ == "__main__":
    question = input("ask a question")
    answer = ask_question(question)
    print("\nAnswer")
    print(answer)