from gateway.views.base_view import BaseMesssage

class DeleteOk(BaseMesssage):
    error_code = 0
    http_code = 204
    
    def __init__(self, message="Deleted"):
        self._message = message
        super(DeleteOk, self).__init__(self)
    
    def _get_msg(self):
        return dict(msg=self._message)

class Ok(BaseMesssage):
    error_code = 0
    http_code = 200
    
    def __init__(self, message="Ok"):
        self._message = message
        super(Ok, self).__init__(self)
    
    def _get_msg(self):
        return dict(msg=self._message)
