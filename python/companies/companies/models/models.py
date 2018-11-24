import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import sqlalchemy.dialects.postgresql.JSON as JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from companies.models.base import Base
from companies.models.company import Company
from companies.models.tariff import Tariff

class Model(object):
    def __init__(self, host, user, password, databasename):
        self.__engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format(user, password, host, databasename))

    def GetCompanyById(self, controller_id):
        sess = sessionmaker(bind=self.__engine)
        return sess.query(Company).filter_by(id=controller_id)
    
    def GetTariffById(self, tariff_id):
        sess = sessionmaker(bind=self.__engine)
        return sess.query(Tariff).filter_by(id=tariff_id)
