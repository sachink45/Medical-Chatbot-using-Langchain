from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from helper import create_rag_chain

# Create FastAPI app
app = FastAPI(title="Medical RAG Assistant")

# Initialize RAG pipeline once at startup
rag_chain = create_rag_chain()



# Request Model

class QuestionRequest(BaseModel):
    question: str


# Routes

@app.get("/")
def home():
    return {"message": "Medical RAG Assistant Running"}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question

    if not question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    response = rag_chain.invoke(question)

    return {
        "question": question,
        "answer": response
    }
