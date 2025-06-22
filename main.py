from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from agents.tutor_agent import TutorAgent

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="AI Tutor Agent", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize the tutor agent
tutor_agent = TutorAgent()


class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    answer: str
    question: str


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML page."""
    try:
        with open("static/index.html", "r") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>AI Tutor Agent</h1><p>Static files not found.</p>")


@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """Handle question requests via JSON POST."""
    try:
        if not request.question or not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        answer = await tutor_agent.answer_question(request.question.strip())
        
        return QuestionResponse(
            question=request.question,
            answer=answer
        )
        
    except Exception as e:
        print(f"Error processing question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.post("/ask-form")
async def ask_question_form(question: str = Form(...)):
    """Handle question requests via form POST."""
    try:
        if not question or not question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        answer = await tutor_agent.answer_question(question.strip())
        
        return QuestionResponse(
            question=question,
            answer=answer
        )
        
    except Exception as e:
        print(f"Error processing form question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "ai_tutor_agent"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 