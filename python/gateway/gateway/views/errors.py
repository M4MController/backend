from gateway.views.base_view import BaseMesssage

class InvalidRequest(BaseMesssage):
    error_code = 1
    http_code = 400
    def __init__(self, message):
        self._message = message
        super(InvalidRequest, self).__init__(self)
    
    def _get_msg(self):
        return dict(msg=self._message)

class NotFound(BaseMesssage):
    error_code = 2
    http_code = 404
    def __init__(self, message):
        self._message = message
        super(NotFound, self).__init__(self)
    
    def _get_msg(self):
        return dict(msg=self._message)