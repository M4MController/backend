from users.models import models
from users.models import user
from users.models import passport
from pymongo import MongoClient

def main():
    mgocli = MongoClient("mongodb://127.0.0.1:27017/")
    udb = models.UserDb(mgocli["user_database"])
    # {"code":0,
    #    "msg":{
    #           "family_name":"Иванов",
    #           "name":"Иван",
    #           "second_name":"Иванович",
    #           "date_receiving":null,
    #           "issued_by":"1961-06-16",
    #           "division_number":null,
    #           "registration_address":"Улица Пушкина, Дом Колотушкина",
    #           "mailing_address":"Улица Пушкина, Дом Колотушкина",
    #           "birth_day":null,
    #           "sex":null,
    #           "home_phone":"111 555",
    #           "mobile_phone":"8 800 555 35 35",
    #           "citizenship":"Албания",
    #           "email":"ml@gmail.com"
    #         }
    # }
    # family_name
    # name
    # second_name
    # passport
    # registration_addres
    # mailing_addres
    # birth_day
    # sex
    # home_phone
    # mobile_phone
    # citizenship
    # e_mail
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