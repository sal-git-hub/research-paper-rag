import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

CHROMA_DB_DIR = "chroma_db"

CHUNK_SIZE = 800

CHUNK_OVERLAP = 100

TOP_K = 4

LLM_MODEL = "llama-3.1-8b-instant"