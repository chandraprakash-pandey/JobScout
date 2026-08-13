from langchain_google_genai import ChatGoogleGenerativeAI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = FastAPI()


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


jobs = [
    {
        "id": 1,
        "title": "Python Developer Intern",
        "company": "ABC Technologies",
        "location": "Pune",
        "source": "LinkedIn"
    },
    {
        "id": 2,
        "title": "AI Engineer Intern",
        "company": "XYZ AI",
        "location": "Remote",
        "source": "Indeed"
    },
    {
        "id": 3,
        "title": "React Developer",
        "company": "Tech Solutions",
        "location": "Mumbai",
        "source": "Wellfound"
    }
]


# Data received from React
class SearchRequest(BaseModel):
    query: str

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0.3)

@app.get("/")
def home():
    return {
        "message": "Welcome to JOBSCOUT!"
    }


@app.get("/jobs")
def get_jobs():
    return {
        "jobs": jobs
    }


@app.post("/search")
def search_jobs(data: SearchRequest):

    print("User Query:", data.query)

    # Use the LLM to process the query
    response = llm.invoke(data.query)

    print("LLM Response:", response.content[0]['text'])

    return {
        "message": "Query received successfully",
        "query": data.query,
        "response": response.content[0]['text']
    }