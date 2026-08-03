# 📚 Research Paper RAG Assistant

## Overview

Research Paper RAG Assistant is an AI-powered application that allows users to upload research papers in PDF format and ask questions about their content. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from the document before generating responses with a Large Language Model.

---

## Features

- Upload PDF research papers
- Ask natural language questions
- Retrieval-Augmented Generation (RAG)
- ChromaDB vector database
- HuggingFace sentence embeddings
- Groq Llama 3.1 integration
- Conversation history
- Source page references
- Download generated responses

---

## Technologies Used

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq API
- PyMuPDF

---

## Project Structure

```
research-paper-rag/
│
├── app.py
├── ingest.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
├── db/
│
└── utils/
    ├── pdf_loader.py
    ├── text_splitter.py
    ├── embeddings.py
    ├── vector_store.py
    └── rag_chain.py
```

---

## Installation

```bash
git clone <repository_url>

cd research-paper-rag

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Run

```bash
streamlit run app.py
```

---

## RAG Pipeline

PDF Upload

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Retriever

↓

Groq LLM

↓

Generated Answer

---

## Embedding Model

sentence-transformers/all-MiniLM-L6-v2

---

## Vector Database

ChromaDB

---

## LLM

Llama 3.1 8B (Groq)

---

## Future Improvements

- Multiple PDF support
- Citation highlighting
- OCR support
- Image-based RAG
- Better retrieval ranking

---

## Author

Saleha Shaikh
