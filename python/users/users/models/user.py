class User(object):
    def __init__(self, family_name, name, second_name, 
                 passport, registration_addres, mailing_addres,
                 birth_day, sex, home_phone, mobile_phone,
                 citizenship, e_mail, id_=None):
        self. id = id_
        self.family_name = family_name
        self.name = name
        self.second_name = second_name
        self.passport = passport
        self.registration_address = registration_addres
        self.mailing_addres = mailing_addres
        self.birth_day = birth_day
        self.sex = sex
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.citizenship = citizenship
        self.e_mail = e_mail

    def get_fields(self):
        return {
            "id": self.id,
            "family_name": self.family_name,
            "name": self.name,
            "second_name": self.second_name,
            "passport": self.passport.get_fields(),
            "registration_addres": self.registration_address,
            "mailing_addres": self.mailing_addres,
            "birth_day": self.birth_day,
            "sex": self.sex,
            "home_phone": self.home_phone,
            "mobile_phone": self.mobile_phone,
            "citizenship": self.citizenship,
            "e_mail": self.e_mail,
        }
