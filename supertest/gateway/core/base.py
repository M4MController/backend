import pytest
import requests
from core import core


class BaseTest(object):
    _auth_prefix='http://127.0.0.1:4999'
    _api_prefix='http://127.0.0.1:5000'

    @classmethod
    def setup_class(cls):
        # добавить авторазвёртывание кластера с healthcheck
        pass
    
    def setup_method(self, method):
        # добавить раскатывание фикстурок
        self.auth = core.HttpClient(self._auth_prefix)
        self.api_raw = core.HttpClient(self._api_prefix)

class AuthorisedTest(BaseTest):
    def get_token(self, username='ml@gmail.com', password='123456'):
        res = self.auth.post('/sign_in', json={
            "e_mail": username,
	        "password": password
        })
        return res.body

    @classmethod
    def setup_class(cls):
        super(AuthorisedTest, cls).setup_class()
    
    def setup_method(self, method):
        super().setup_method(method)
        self.token = self.get_token()
        self.api = core.TokenWrapper(self.api_raw, self.token)