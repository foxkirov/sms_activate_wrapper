from smsactivate.api import SMSActivateAPI
from time import sleep
from pysmsactivate.errors import *


class Activation(object):
    def __init__(self, api_key: str, country: int, service: str = "tg", debug: bool = False):
        self.sa = SMSActivateAPI(api_key)
        self.sa.debug_mode = debug
        self.country = country
        self.service = service
        self.debug = debug
        self.number = None
        self.activation_id = None

    def errors_interceptor(self, response: dict):

        if isinstance(response, dict) and 'error' in response.keys():
            if response['error'] == "NO_NUMBERS":
                raise NoNumbersError(text=response)

            elif 'message' in response.keys() and response['message'] == 'Server error, try again':
                raise ServerError

            else:
                if self.debug:
                    print(response)
                raise UnknownError(text=response['error'], message=response['message'])
        else:
            return response

    def get_numbers_count(self):
        response = self.sa.getNumbersStatus(country=self.country)
        if self.debug:
            print(response[f"{self.service}_0"])

        return response

    def get_number(self, retry_count: int = 10):
        i = 0
        while True:
            i += 1

            activation = self.sa.getNumber(service=self.service,
                                           country=self.country,
                                           forward=False)  # {'activation_id': 000000000, 'phone': 79999999999}

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
