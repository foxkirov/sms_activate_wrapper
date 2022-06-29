
class UnknownError(Exception):
    def __init__(self, text, message):
        self.txt = text
        self.message = message


class NoNumbersError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "NO_NUMBERS"
        self.message = "There are no free numbers for receiving SMS from the current service"


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


class BadStatusError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "BAD_STATUS"
        self.message = "Attempt to establish a non-existent status"


class StatusCancelError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "STATUS_CANCEL"
        self.message = "Current activation canceled and no longer available"


class BannedError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "BANNED"
        self.message = "Account is blocked"


class NoConnectionError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "NO_CONNECTION"
        self.message = "No connection to servers"


class AccountInactiveError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "ACCOUNT_INACTIVE"
        self.message = "No numbers available"


class NoIdRentError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "NO_ID_RENT"
        self.message = "Rent id not specified"


class InvalidPhoneError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "INVALID_PHONE"
        self.message = "The number was not rented by you (wrong rental id)"


class StatusFinishError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "STATUS_FINISH"
        self.message = "Rent paid and completed"


class StatusCanceledError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "STATUS_CANCEL"
        self.message = "Rent canceled with a refund"


class StatusIncorrectError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "INCORRECT_STATUS"
        self.message = "Missing or incorrect status"


class StatusCanNotCancelError(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = "CANT_CANCEL"
        self.message = "Unable to cancel the lease (more than 20 minutes have passed)"


