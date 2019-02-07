import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import sqlalchemy.dialects.postgresql.json as json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from companies.models.base import Base
from companies.models.company import Company
from companies.models.tariff import Tariff

class Model(object):
    def __init__(self, host, user, password, databasename):
        self._engine = create_engine('postgresql://{}:{}@{}/{}'.format(user, password, host, databasename))

    def GetCompanyById(self, company_id):
        sessM = sessionmaker(bind=self._engine)
        sess = sessM()
        return sess.query(Company).filter_by(id=company_id).one()

    def GetTariffById(self, tariff_id):
        sessM = sessionmaker(bind=self._engine)
        sess = sessM()
        return sess.query(Tariff).filter_by(id=tariff_id).one()

    def GetFullCompanyInfo(self, company_id):
        sessM = sessionmaker(bind=self._engine)
        sess = sessM()
        return sess.query(Company, Tariff).filter_by(id=company_id).all()

    def InsertCompany(self, name, address, phone, bank_account_id):
        sessM = sessionmaker(bind=self._engine, autocommit=True)
        sess = sessM()
        sess.begin()
        cpny = Company(name=name,
                        address=address,
                        phone=phone,
                        bank_account_id=bank_account_id)
        try:
            sess.add(cpny)
        except Exception as e:
            sess.rollback()
            return "ERROR {}".format(str(e))
        sess.commit()
        sess.flush()
        sess.refresh(cpny)
        return cpny

    def InsertTariff(self, name, val, company):
        sessM = sessionmaker(bind=self._engine, autocommit=True)
        sess = sessM()
        sess.begin()
        trf = Tariff(name=name,
                    val=val,
                    company=company)
        try:
            sess.add(trf)
        except Exception as e:
            sess.rollback()
            return "ERROR {}".format(str(e))
        sess.commit()
        sess.flush()
        sess.refresh(trf)
        return trf
