from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class Book(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('book_id_seq'), primary_key=True)
    name = Column(String(50))
    isbn = Column(String(12))
    title = Column(String(120))
