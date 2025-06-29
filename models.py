from datetime import datetime
from sqlalchemy import String, Integer, Text, Column, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "crud_users"

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True, nullable=False)
    name = Column(String(32),nullable=False)
    age = Column(Integer, nullable=True)
    mobile_number = Column(String(16), nullable=True)
    address = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.now(), nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.now(), nullable=True)
