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
    

class Books(Base):
    """
    TODO:Thi is a db table the books
        :param title: str. This is a name book.
        :param author: str.
        :param year: int. This is a year when this is book was created.
        :param status: is "в наличии" or "выдана"
    """
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    author = Column(String, default="anonim")
    year = Column(Integer, nullable=False)
    status = Mapped[Status]
    
# Create an engine
engine = create_engine(DATABASE_URL)
Base.metadata.create_all()
Session = sessionmaker(bind=engine)

def get_session():
    return Session()