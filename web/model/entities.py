from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector

class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    code = Column(String(10))
    name = Column(String(15))
    surname = Column(String(30))
    password = Column(String(12))
