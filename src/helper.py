from typing import List
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from store_index import get_retriever
import config



# Document Loader

def document_loader(data_path):
    loader = DirectoryLoader(
        data_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    return loader.load()


def extract_page_content(docs: List[Document]) -> List[Document]:
    minimal_docs = []

    for doc in docs:
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": doc.metadata.get("source")}
            )
        )

    return minimal_docs



# Chunking

def chunk_documents(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP
    )

    return splitter.split_documents(docs)


# RAG Pipeline

def create_rag_chain():

    llm = ChatOpenAI(
        model=config.LLM_MODEL_NAME,
        temperature=config.TEMPERATURE
    )

    retriever = get_retriever()

    system_prompt = """
    You are a medical assistant.
    Use the retrieved context to answer the question.
    If unsure, say you do not have sufficient information.
    Keep answers short and simple (3-4 sentences).

    Context: {context}
    Question: {question}
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{question}")
    ])

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
