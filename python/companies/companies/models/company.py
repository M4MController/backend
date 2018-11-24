import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import sqlalchemy.dialects.postgresql.JSON as JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from companies.models.base import Base

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    bank_account_id = Column(String)
