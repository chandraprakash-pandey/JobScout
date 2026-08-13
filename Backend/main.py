from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

    return {
        "message": "Query received successfully",
        "query": data.query
    }