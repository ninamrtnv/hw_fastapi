from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from settings.settings import DATABASE_DSN

Base = declarative_base()
pg_session = scoped_session(sessionmaker(bind=create_engine(DATABASE_DSN)))