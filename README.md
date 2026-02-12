# 🏥 Medical Chatbot using LangChain (RAG Based)

An AI-powered Medical Question Answering system built using **Retrieval-Augmented Generation (RAG)** architecture with **LangChain, OpenAI, Pinecone, and FastAPI**.

This project processes medical documents, stores their embeddings in a vector database, and generates grounded responses to user queries.

---

## 🚀 Project Overview

This application:

- Loads and processes medical PDF documents
- Splits documents into semantic chunks
- Converts chunks into vector embeddings using OpenAI
- Stores embeddings in Pinecone (Vector Database)
- Retrieves relevant chunks using cosine similarity
- Generates contextual answers using GPT
- Exposes the system via a FastAPI backend

---

## 🧠 Architecture

Medical-Chatbot-using-Langchain/
│
├── src/
│ ├── app.py # FastAPI application
│ ├── main.py # Entry point
│ ├── helper.py # RAG pipeline logic
│ ├── create_vector.py # Pinecone index & vector store
│ └── config.py # Configuration variables
│
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md


## 🛠 Tech Stack

- **Python**
- **LangChain**
- **OpenAI Embeddings (text-embedding-3-small)**
- **Pinecone Vector Database**
- **FastAPI**
- **Docker**
- **AWS (Planned Deployment)**

---



## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sachink45/Medical-Chatbot-using-Langchain.git
cd Medical-Chatbot-using-Langchain


##Create Virtual Environment
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows

##Install Dependencies
pip install -r requirements.txt

##Set Environment Variables
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key

##Run the Application
uvicorn app:app --reload

## Open in browser:
http://127.0.0.1:8000/docs
```




