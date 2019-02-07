from pymongo import MongoClient
from models import passport 
from models import user

class UserDb(object):
    def __init__(self, database):
        self.__mgocli = database

    def get_user_by_id(self, user_id):
        uinf = self.__mgocli.users.find_one({"id": user_id})
        doc = passport.Passport(issued_by=uinf["passport"]["issued_by"],
                                date_receiving=int(uinf["passport"]["date_receiving"]),
                                division_number=uinf["passport"]["division_number"])
        result = user.User(family_name=uinf["family_name"],
                           name=uinf["name"],
                           second_name=uinf["second_name"],
                           passport=doc,
                           registration_addres=uinf["registration_addres"],
                           mailing_addres=uinf["mailing_addres"],
                           birth_day=uinf["birth_day"],
                           sex=uinf["sex"],
                           home_phone=uinf["home_phone"],
                           mobile_phone=uinf["mobile_phone"],
                           citizenship=uinf["citizenship"],
                           e_mail=uinf["e_mail"])
        return result

    
    def insert_user(self, user):
        # TODO: не потокобезопасно переписать 
        db = self.__mgocli.users
        #new_id = self.__mgocli.users.count_documents({}) + 1
        new_id = self.__mgocli.users.find().count() + 1
        user.id = new_id
        self.__mgocli.users.insert_one(user.get_fields())
        return user