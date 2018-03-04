from flask_json import JsonError


class HttpException(JsonError):
    def __init__(self, code, title, description=''):
        super(HttpException, self).__init__(
            code,
            title=title,
            description=description,
        )


class BadRequestException(HttpException):
    def __init__(self, description=''):
        super(BadRequestException, self).__init__(
            400,
            'Bad request',
            description
        )


class NotFoundException(HttpException):
    def __init__(self, description=''):
        super(NotFoundException, self).__init__(
            404,
            'Not found',
            description
        )


class ControllerNotFoundException(NotFoundException):
    def __init__(self):
        super(ControllerNotFoundException, self).__init__('Controller not found')


class SensorNotFoundException(NotFoundException):
    def __init__(self):
        super(SensorNotFoundException, self).__init__('Controller not found')


class InvalidAgrumentsException(BadRequestException):
    def __init__(self, messages):
        super(InvalidAgrumentsException, self).__init__(
            messages
        )


class InternalErrorException(HttpException):
    def __init__(self, description=''):
        super(InternalErrorException, self).__init__(
            500,
            'Internal server error',
            description
        )


class NotImplementedException(HttpException):
    def __init__(self, description=''):
        super(NotImplementedException, self).__init__(
            501,
            'Not implemented',
            description
        )
