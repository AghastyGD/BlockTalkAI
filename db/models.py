from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text, create_engine, Enum as SqlEnum, Table
from sqlalchemy.orm import relationship
from .config import Base, engine
from enum import Enum
import uuid_utils as uuid
from sqlalchemy.dialects.postgresql import UUID

class JobLevelEnum(str, Enum):
    junior = "jr"
    mid = "md"
    senior = "sr"

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid.uuid7()), unique=True, nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=False)
    responsibilities = Column(Text, nullable=False)
    level = Column(SqlEnum(JobLevelEnum), nullable=False)
    skills = relationship("Skill", secondary="job_skills", back_populates="jobs")

    def __repr__(self):
        return f"<Job(title={self.title}, level={self.level})>"
    
    
job_skills = Table('job_skills', Base.metadata,
    Column('job_id', String, ForeignKey('jobs.id')),
    Column('skill_id', String, ForeignKey('skills.id'))
)

class Skill(Base):
    __tablename__ = 'skills'

    id = Column(String, primary_key=True, index=True)
    title = Column(String(100), unique=True, nullable=False)
    jobs = relationship("Job", secondary=job_skills, back_populates="skills")

    def __repr__(self):
        return f"<Skill(title={self.title})>"

Base.metadata.create_all(engine)



