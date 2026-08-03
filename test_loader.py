from utils.pdf_loader import load_pdf

docs = load_pdf("data/attention_is_all_you_need.pdf")

print(f"Loaded {len(docs)} pages\n")

print("First page:\n")
print(docs[0].page_content[:500])

print("\nMetadata:")
print(docs[0].metadata)