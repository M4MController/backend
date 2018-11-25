from sqlalchemy import create_engine
from sqlalchemy import MetaData
from companies.models.models import Model
from companies.config import ConfigManager
from companies.models.tariff import MonoTariffVal

def main():
    confs = ConfigManager()
    dbconf = confs["database"]
    model = Model(
        host="127.0.0.1",
        user=dbconf["username"],
        password=dbconf["password"],
        databasename=dbconf["database"])
    company = model.InsertCompany(name="plain_name",
                        address="plain_address",
                        phone="plain_address",
                        bank_account_id="plain_bank_acc_id")
    tariff = model.InsertTariff(name="name",
                        val=MonoTariffVal(1),
                        company=company.id)
    tariff2 = model.InsertTariff(name="name_2",
                        val=MonoTariffVal(1),
                        company=company.id)
    cpns = model.GetCompanyById(company.id)
    print("Companies:")
    print(str(cpns))
    tariffs = model.GetTariffById(tariff.id)
    print("Tariffs:")
    print(str(tariffs))
    full_info = model.GetFullCompanyInfo(company.id)
    print("Full info:")
    for comp, tariff in full_info:
        print(comp)
        print(tariff)

if __name__ == "__main__":
    main()
