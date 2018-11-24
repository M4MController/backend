import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import sqlalchemy.dialects.postgresql.JSON as JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from companies.models.base import Base

class Tariff(Base):
    __tablename__ = 'tariff'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tariff_type = Column(Integer)
    vals = Column(JSON)
    compnany = Column(Integer, ForeignKey('companies.id'))
