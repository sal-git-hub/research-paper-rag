from utils.vector_store import load_vector_store

question = input("Ask a question: ")

vector_store = load_vector_store()
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

docs = retriever.invoke(question)

print("\nRetrieved chunks:\n")

for i, doc in enumerate(docs, 1):
    print(f"Chunk {i}")
    print("-" * 40)
    print(doc.page_content[:800])
    print("\nMetadata:", doc.metadata)
    print()