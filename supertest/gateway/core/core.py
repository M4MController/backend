import requests
import json
from core import exceptions

class Request:
    def __init__(self, url, method):
        self.url = url
        self.method = method

    def __repr__(self):
        return "{}:{} \n\n".format(self.method, self. url)


class GetRequest(Request):
    def __init__(self, url, params):
        super().__init__(url, "GET")

class PostRequest(Request):
    def __init__(self, url, params):
        super().__init__(url, "POST")
        self.params = params
    
    def __repr__(self):
        return super().__repr__() + "\n Args is: {}\n".format(json.dumps(self.params, indent=4))


class Response:
    def __init__(self, code, body, req):
        self.code = code
        self.body = body
        self.req = req
    
    def json(self):
        try:
            return json.loads(self.body)
        except json.JSONDecodeError as err:
            raise exceptions.ResponseParsingError(self, str(err))
    
    def __resp_part(self):
        return "code: {} \n body: {} \n".format(self.code, self.body)
    
    def __repr__(self):
        requestmsg = str(self.req)
        respmsg = self.__resp_part()
        return requestmsg + respmsg



class HttpClient:
    def __init__(self, host):
        self._base = host
        self._sess = requests.Session()
    
    def get(self, path, **kwargs):
        rsp = self._sess.get(self._base + path, **kwargs)
        return Response(rsp.status_code, rsp.text, GetRequest(rsp.url, kwargs))
    
    def post(self, path, **kwargs):
        rsp = self._sess.post(self._base + path, **kwargs)
        return Response(rsp.status_code, rsp.text, PostRequest(rsp.url, kwargs))

class TokenWrapper:
    def __init__(self, api, token):
        self._api = api
        self._token = token
    
    def get(self, path, **kwargs):
        if "params" not in kwargs:
            kwargs["params"] = {"token": self._token}
        else:
            if "token" not in kwargs["params"]:
                kwargs["params"]["token"] = self._token
        return self._api.get(path, **kwargs)
    
    def post(self, path, **kwargs):
        if "params" not in kwargs:
            kwargs["params"] = {"token": self._token}
        else:
            if "token" not in kwargs["params"]:
                kwargs["params"]["token"] = self._token
        return self._api.post(path, **kwargs)
