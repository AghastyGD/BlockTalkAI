from fastapi import FastAPI
from schemas.job import JobCreateRequest
from db.config import session
from db.models import Job

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Chat Interview API"}

@app.post("/create-job")
async def create_job(job_request: JobCreateRequest):
    job = Job(
        title=job_request.title,
        description=job_request.description,
        requirements=job_request.requirements,
        responsibilities=job_request.responsibilities,
        level=job_request.level
    )
    session.add(job)
    session.commit()
    return job

@app.get("/jobs")
async def job_list():
    jobs_query = session.query(Job)
    
    return jobs_query.all()

