import abc

class BaseMesssage(object):
    error_code = -1
    http_code = -1
    def __init__(self, message):
        self.message = message

    @abc.abstractmethod
    def _get_msg(self):
        pass

    def get_message(self):
        dct = dict(code=self.error_code,
                    msg=self._get_msg())
        return dct, self.http_code
