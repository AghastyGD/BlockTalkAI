from pydantic import BaseModel
from db.models import JobLevelEnum
from typing import List

class JobCreateRequest(BaseModel):
    title: str
    description: str
    requirements: str
    responsibilities: str
    level: JobLevelEnum
    skill_ids: List[str]