from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.vector_store import create_vector_store


def ingest_pdf(pdf_path):
    docs = load_pdf(pdf_path)
    chunks = split_documents(docs)
    create_vector_store(chunks)


if __name__ == "__main__":
    ingest_pdf("data/attention_is_all_you_need.pdf")