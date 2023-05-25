from sqlalchemy import create_engine
# For Creating Base
from sqlalchemy.ext.declarative import declarative_base
# For Session
from sqlalchemy.orm import sessionmaker

# DB Location variable
SQLALCHEMY_DATABASE_URL = 'sqlite:///./data.db'

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

# Creating Session
LocalSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Initialising base
Base = declarative_base()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
