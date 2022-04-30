# sms_activate_wrapper
Basic usage:

```
from pysmsactivate import Activation

activation = Activation(api_key="my_api_key", service="vk", country=0)

activation.get_numbers_count()

number = activation.get_number(retry_count=100)

sms_code = activation.wait_code(3600)

print(f"code: {sms_code}")

print(activation.close())
```