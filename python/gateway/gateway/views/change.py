from gateway.views.base_view import BaseMesssage

class Posted(BaseMesssage):
    error_code = 0
    http_code = 200
    def __init__(self):
        super(Posted, self).__init__(self)

    def _get_msg(self):
        return dict(error_message="Ok")