from pymongo import MongoClient
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    born_date = Column(Date)
    born_location = Column(String(100))
    description = Column(Text)

class Quote(Base):
    __tablename__ = 'quotes'
    
    id = Column(Integer, primary_key=True)
    quote = Column(Text)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="quotes")

Author.quotes = relationship("Quote", order_by=Quote.id, back_populates="author")

# Подключение к MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['your_mongo_database']
authors_collection = mongo_db['authors']
quotes_collection = mongo_db['quotes']

# Извлечение данных
authors = list(authors_collection.find())
quotes = list(quotes_collection.find())

# Подключение к PostgreSQL
engine = create_engine('postgresql://your_username:your_password@localhost/your_postgres_database')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Перенос данных
for author in authors:
    new_author = Author(
        full_name=author['full_name'],
        born_date=author.get('born_date'),
        born_location=author.get('born_location'),
        description=author.get('description', '')
    )
    session.add(new_author)
    session.commit()  # Сохраните автора, чтобы получить его id

    for quote in quotes:
        if quote['author_id'] == author['_id']:
            new_quote = Quote(quote=quote['quote'], author=new_author)
            session.add(new_quote)

session.commit()
session.close()
mongo_client.close()