import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from utils.vector_store import load_vector_store

load_dotenv()


def get_rag_response(question):
    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a helpful research paper assistant.

Answer ONLY using the context below.

If the answer is not in the context, say:
"I couldn't find that information in the uploaded paper."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY"),
    )

    response = llm.invoke(
        prompt.format(
            context=context,
            question=question,
        )
    )

    return response.content, docs