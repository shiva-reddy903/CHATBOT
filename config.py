import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DATA_PATH = "data"
UPLOAD_FOLDER = "uploaded_files"
VECTOR_DB_PATH = "vector_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "llama3.2:latest"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 8