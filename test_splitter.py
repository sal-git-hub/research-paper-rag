from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents

docs = load_pdf("data/attention_is_all_you_need.pdf")

chunks = split_documents(docs)

print(f"Pages Loaded: {len(docs)}")
print(f"Chunks Created: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print("\nMetadata:")
print(chunks[0].metadata)