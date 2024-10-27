from sqlalchemy import Date, create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    born_date = Column(Date)  # Измените на Date, если хотите
    born_location = Column(String(100))
    description = Column(Text)

class Quote(Base):
    __tablename__ = 'quotes'
    
    id = Column(Integer, primary_key=True)
    quote = Column(Text)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="quotes")

Author.quotes = relationship("Quote", order_by=Quote.id, back_populates="author")
