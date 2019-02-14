class TestException(Exception):
    def __init__(self, response, error_message):
        self.response = response
        self.error_message = error_message
        super().__init__(str(self.response) + str(error_message))

class ResponseParsingError(TestException):
    pass