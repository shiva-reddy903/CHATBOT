import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import (
    DATA_PATH,
    UPLOAD_FOLDER,
    VECTOR_DB_PATH,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def load_documents():

    documents = []

    folders = [DATA_PATH, UPLOAD_FOLDER]

    for folder in folders:

        if not os.path.exists(folder):
            continue

        for file in os.listdir(folder):

            if file.lower().endswith(".pdf"):

                file_path = os.path.join(folder, file)

                print(f"Loading: {file}")

                loader = PyPDFLoader(file_path)

                docs = loader.load()

                for doc in docs:
                    doc.metadata["source"] = file

                documents.extend(docs)

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)


def create_vector_database():

    documents = load_documents()

    if len(documents) == 0:
        print("No PDF files found.")
        return

    chunks = split_documents(documents)

    print(f"Total Pages : {len(documents)}")
    print(f"Total Chunks : {len(chunks)}")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    if os.path.exists(VECTOR_DB_PATH):
        shutil.rmtree(VECTOR_DB_PATH, ignore_errors=True)

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    print("Vector database created successfully!")


if __name__ == "__main__":
    create_vector_database()