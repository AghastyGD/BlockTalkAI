from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

url = URL.create(
    drivername = "postgresql",
    username = "user",
    password = "pass",
    host = "localhost",
    database = "db",
    port = 5432,
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

