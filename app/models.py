from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text, INTEGER

class Product(Base):
    __tablename__ = 'product'
    id = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(String,  nullable=False)
    create_time = Column(TIMESTAMP,  nullable=True)
    price = Column(INTEGER,  nullable=True)