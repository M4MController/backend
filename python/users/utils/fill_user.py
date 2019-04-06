from users.models import models
from users.models import user
from users.models import passport
from pymongo import MongoClient
import argparse

def main():
    parser = argparse.ArgumentParser(description='Сгенерировать данные')
    parser.add_argument('--connection', '-c', type=str, default="localhost:27017", help='часть для connection string')
    args = parser.parse_args()
    
    mgocli = MongoClient('mongodb://{}/'.format(args.connection))
    databasename = "user_database"
    mgocli.drop_database(databasename)
    db = mgocli[databasename]
    udb = models.UserDb(db)
    uins = user.User(
               family_name="Иванов",
               name="Иван",
               second_name="Иванович",
               passport=passport.Passport(
                    date_receiving=156,
                    issued_by="1961-06-16",
                    division_number="DIVNUM",
               ),
               registration_addres="Улица Пушкина, Дом Колотушкина",
               mailing_addres="Улица Пушкина, Дом Колотушкина",
               birth_day="156",
               sex=0,
               home_phone="111 555",
               mobile_phone="8 800 555 35 35",
               citizenship="Албания",
               e_mail="ml@gmail.com"
    )
    ins_user = udb.insert_user(uins)

if __name__ == "__main__":
    main()