import fitz  # PyMuPDF
from langchain_core.documents import Document


def load_pdf(file_path):
    """
    Loads a PDF and returns a list of LangChain Documents.
    Each page becomes one Document with page metadata.
    """

    pdf = fitz.open(file_path)
    documents = []

    for page_num, page in enumerate(pdf):
        text = page.get_text()

        if text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": file_path,
                        "page": page_num + 1,
                    },
                )
            )

    pdf.close()
    return documents