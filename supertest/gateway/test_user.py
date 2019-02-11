from core.base import BaseTest, AuthorisedTest

class TestCase(AuthorisedTest):
    def test_get_user_info(self):
        result = self.api.get('/user/user_info')
        print(result)
        assert result.json() == { 
            "code":0, 
            "msg": {
                "family_name": "\u0418\u0432\u0430\u043d\u043e\u0432",
                "name": "\u0418\u0432\u0430\u043d",
                "second_name": "\u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447",
                "date_receiving": 156,
                "issued_by": "1961-06-16",
                "division_number": "DIVNUM",
                "registration_addres": "\u0423\u043b\u0438\u0446\u0430 \u041f\u0443\u0448\u043a\u0438\u043d\u0430, \u0414\u043e\u043c \u041a\u043e\u043b\u043e\u0442\u0443\u0448\u043a\u0438\u043d\u0430",
                "mailing_addres": "\u0423\u043b\u0438\u0446\u0430 \u041f\u0443\u0448\u043a\u0438\u043d\u0430, \u0414\u043e\u043c \u041a\u043e\u043b\u043e\u0442\u0443\u0448\u043a\u0438\u043d\u0430",
                "birth_day": "156",
                "sex": False,
                "home_phone": "111 555",
                "mobile_phone": "8 800 555 35 35",
                "citizenship": "\u0410\u043b\u0431\u0430\u043d\u0438\u044f",
                "e_mail": "ml@gmail.com"
            }
        }
