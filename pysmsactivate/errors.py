
class UnknownError(Exception):
    def __init__(self, text, message):
        self.txt = text
        self.message = message


class NoNumbersError(Exception):
    def __init__(self, text):
        self.txt = text


class ServerError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "SERVER_ERROR"
        self.message = "Server error, try again"


class NoBalanseError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "NO_BALANCE"
        self.message = "Not enough funds"


class BadActionError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "BAD_ACTION"
        self.message = "Invalid action (action parameter)"


class BadServiceError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "BAD_SERVICE"
        self.message = "Incorrect service name (service parameter)"


class BadKeyError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "BAD_KEY"
        self.message = "Invalid API access key"


class SqlError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "ERROR_SQL"
        self.message = "One of the parameters has an invalid value."


class NoActivationError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "NO_ACTIVATION"
        self.message = "The specified activation id does not exist"

