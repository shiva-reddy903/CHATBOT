import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_AI_KEY = os.getenv("OPENAI_API_KEY")

DATA_PATH = "data"
VECTOR_DB_PATH = "vector_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "gpt-3.5-turbo"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200