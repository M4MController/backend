from sqlalchemy import create_engine
from sqlalchemy import MetaData
from companies.models.models import Model
from companies.config import ConfigManager

def main():
    confs = ConfigManager()
    dbconf = confs["database"]
    model = Model(
        host="127.0.0.1",
        user=dbconf["username"],
        password=dbconf["password"],
        databasename=dbconf["database"])
    model.GetCompanyById(1)
    model.GetTariffById(1)
    model.GetFullCompanyInfo(1)

if __name__ == "__main__":
    main()
