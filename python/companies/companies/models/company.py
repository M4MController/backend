import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.dialects.postgresql.json import JSON
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

    def __repr__(self):
        return """
            {{
                "id": {},
                "name": {},
                "address": {},
                "phone": {},
                "bank_account_id": {}
            }}
        """.format( self.id,
                    self.name,
                    self.address,
                    self.phone,
                    self.bank_account_id)
