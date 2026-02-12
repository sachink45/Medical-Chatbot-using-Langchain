# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# API Keys

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Model Configuration

EMBEDDING_MODEL_NAME = "text-embedding-3-small"
LLM_MODEL_NAME = "gpt-3.5-turbo"
TEMPERATURE = 0.3   


# Pinecone Configuration

INDEX_NAME = "medical-chatbot"
VECTOR_DIMENSION = 1536
METRIC = "cosine"
CLOUD = "aws"
REGION = "us-east-1"


# Chunking Configuration

CHUNK_SIZE = 850
CHUNK_OVERLAP = 100


# Retriever Configuration

TOP_K = 3
