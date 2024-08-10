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

    def __repr__(self):
        return f"<Job(title={self.title}, level={self.level})>"
    
Base.metadata.create_all(engine)



