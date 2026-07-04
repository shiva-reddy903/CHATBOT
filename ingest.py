from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from config import(
    DATA_PATH,
    VECTOR_DB_PATH,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)
def create_vector_database():
    print("Loading PDF files...")
    loader = PyPDFDirectoryLoader(DATA_PATH)
    documents = loader.load()
    print(f"Load {len(documents)} pages.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks.")
    embeddings = HuggingFaceEmbeddings(
        model_name = EMBEDDING_MODEL
    )
    Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory = VECTOR_DB_PATH
    )
    print("Vector database created successfully!")
if __name__ == "__main__":
    create_vector_database()