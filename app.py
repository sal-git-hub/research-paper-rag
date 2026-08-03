import os
import streamlit as st

from ingest import ingest_pdf
from utils.rag_chain import get_rag_response

st.set_page_config(
    page_title="Research Paper RAG Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📚 Research Paper RAG Assistant")

st.caption(
    "Upload a research paper and ask questions using Retrieval-Augmented Generation (RAG)."
)

st.divider()

st.sidebar.title("📂 Upload Research Paper")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

st.sidebar.markdown("---")

st.sidebar.info("""
### Technologies Used

- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq Llama 3.1
- Streamlit
""")

if "uploaded_pdf" not in st.session_state:
    st.session_state.uploaded_pdf = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if uploaded_file is not None:

    if st.session_state.uploaded_pdf != uploaded_file.name:

        os.makedirs("data", exist_ok=True)

        pdf_path = os.path.join("data", uploaded_file.name)

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Processing PDF..."):
            ingest_pdf(pdf_path)

        st.session_state.uploaded_pdf = uploaded_file.name

        st.sidebar.success("✅ PDF uploaded successfully!")
        st.sidebar.write(f"**Current document:** {uploaded_file.name}")

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question about your document...")

if question:

    if st.session_state.uploaded_pdf is None:

        st.warning("Please upload a PDF before asking questions.")
        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Searching the document..."):

        answer, docs = get_rag_response(question)

    with st.chat_message("assistant"):

        st.markdown(answer)

        st.markdown("### 📚 Source Documents")

        shown_pages = set()

        for doc in docs:

            page = doc.metadata.get("page")

            if page in shown_pages:
                continue

            shown_pages.add(page)

            with st.expander(f"📄 Page {page}"):

                st.write(doc.page_content[:700] + "...")

        st.download_button(
            label="⬇ Download Answer",
            data=answer,
            file_name="rag_response.txt",
            mime="text/plain"
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

st.divider()

st.caption(
    "Research Paper RAG Assistant | Built with Streamlit, LangChain, ChromaDB, HuggingFace Embeddings and Groq"
)