from smsactivate.api import SMSActivateAPI
from time import sleep
from pysmsactivate.errors import *


class Activation(object):
    def __init__(self, api_key: str,
                 country: int,
                 service: str = "tg",
                 debug: bool = False,
                 api_url: str = None):

        self.sa = SMSActivateAPI(api_key)
        self.sa.debug_mode = debug
        self.country = country
        self.service = service
        self.debug = debug
        self.number = None
        self.activation_id = None
        if api_url:
            self.sa.__api_url = api_url

    def get_numbers_count(self):
        response = self.sa.getNumbersStatus(country=self.country)

        if self.debug:
            print(response[f"{self.service}"])

        return response

    def get_number(self, retry_count: int = 10):
        i = 0
        while True:
            i += 1

            activation = self.sa.getNumber(service=self.service,
                                           country=self.country,
                                           forward=False)

            if self.debug:
                print(activation)

            try:
                self.errors_interceptor(activation)

            except Exception as e:
                if i <= retry_count:
                    sleep(1)
                else:
                    raise e
            else:
                break

        self.number = activation["phone"]
        self.activation_id = activation["activation_id"]

        return self.number

    def wait_code(self, timeout: int):
        self.errors_interceptor(self.sa.setStatus(id=self.activation_id, status=1))
        i = 0

        while i < timeout:
            i += 1
            sleep(1)
            try:
                status = self.errors_interceptor(self.sa.getStatus(id=self.activation_id))

            except ServerError:
                continue

            st = self.sa.activationStatus(status)

            if self.debug:
                print(st)

            if "STATUS_OK" in st['status']:
                return st['status'].split(":")[1]

        raise TimeoutError("timeout error")

    def cancel(self):
        response = self.errors_interceptor(self.sa.setStatus(id=self.activation_id, status=6))
        return response

    def close(self):
        response = self.errors_interceptor(self.sa.setStatus(id=self.activation_id, status=6))
        return response

    def get_balance(self) -> float:
        response = self.errors_interceptor(self.sa.getBalance())
        return float(response['balance'])

    def errors_interceptor(self, response: dict):

        if isinstance(response, dict) and 'error' in response.keys():
            if response['error'] == "NO_NUMBERS":
                raise NoNumbersError

            elif response['error'] == "NO_BALANCE":
                raise NoBalanseError

            elif response['error'] == "BAD_ACTION":
                raise BadActionError

            elif response['error'] == "BAD_SERVICE":
                raise BadServiceError

            elif response['error'] == "BAD_KEY":
                raise BadKeyError

            elif response['error'] == "ERROR_SQL":
                raise SqlError

            elif response['error'] == "NO_ACTIVATION":
                raise NoActivationError

            elif response['error'] == "BAD_STATUS":
                raise BadStatusError

            elif response['error'] == "STATUS_CANCEL":
                raise StatusCancelError

            elif response['error'] == "BANNED":
                raise BannedError

            elif response['error'] == "NO_CONNECTION":
                raise NoConnectionError

            elif response['error'] == "ACCOUNT_INACTIVE":
                raise AccountInactiveError

            elif response['error'] == "NO_ID_RENT":
                raise NoIdRentError

            elif response['error'] == "INVALID_PHONE":
                raise InvalidPhoneError

            elif response['error'] == "INCORRECT_STATUS":
                raise StatusIncorrectError

            else:
                if self.debug:
                    print(response)
                raise UnknownError(text=response['error'], message=response['message'])

        else:
            return response
