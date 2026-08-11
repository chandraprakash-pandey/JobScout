from fastapi import FastAPI

app = FastAPI()


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