class UnknownError(Exception):
    def __init__(self, text, message):
        self.txt = text
        self.message = message


class NoNumbersError(Exception):
    def __init__(self, text):
        self.txt = text


class ServerError(Exception):
    def __init__(self):
        self.txt = "SERVER_ERROR"
        self.message = "Server error, try again"
