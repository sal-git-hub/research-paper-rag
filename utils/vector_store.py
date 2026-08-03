from langchain_chroma import Chroma
from utils.embeddings import get_embedding_model

DB_DIRECTORY = "db"
COLLECTION_NAME = "research_papers"


def create_vector_store(chunks):
    embeddings = get_embedding_model()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=DB_DIRECTORY,
    )

    try:
        vector_store.delete_collection()
    except:
        pass

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_DIRECTORY,
    )

    return vector_store


def load_vector_store():
    embeddings = get_embedding_model()

    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=DB_DIRECTORY,
    )