from pydantic import BaseModel
from db.models import JobLevelEnum

class JobCreateRequest(BaseModel):
    title: str
    description: str
    requirements: str
    responsibilities: str
    level: JobLevelEnum
