"""Models of db"""
import os
import enum
from sqlalchemy import (create_engine,
                        Column,
                        Integer,
                        String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (Mapped, sessionmaker)
from dotenv_ import DATABASE_URL

# Create the basic class for declarative class
Base = declarative_base()

class Status(enum.Enum):
    """
    This is a db for choose a book status.
    """
    AVAILABILITY = "в наличии"
    ISSUANCE = "выдана"
    

class Book(Base):
    """
    Thi is a db table the books
    """
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    author = Column(String, default="anonim")
    status = Mapped[Status]
    
# Create an engine
engine = create_engine(DATABASE_URL)
Base.metadata.create_all()
Session = sessionmaker(bind=engine)