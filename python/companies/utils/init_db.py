from sqlalchemy import create_engine
from sqlalchemy import MetaData
from companies.models.models import Model
from companies.models.base import Base
from companies.config import ConfigManager

def main():
    confs = ConfigManager()
    dbconf = confs["database"]
    model = Model(
        #host=dbconf["host"],
        host="127.0.0.1",
        user=dbconf["username"],
        password=dbconf["password"],
        databasename=dbconf["database"])
    metadata = MetaData()
    Base.metadata.create_all(model._engine)

if __name__ == "__main__":
    main()
