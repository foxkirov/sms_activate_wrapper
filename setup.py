from setuptools import setup


setup(
    name='pysmsactivate',
    version='0.1.0',
    description='Sms Activate Wrapper Package',
    url='https://github.com/foxkirov/sms_activate_wrapper',
    install_requires=['smsactivate==1.3', 'requests==2.27.1'],
    packages=['pysmsactivate'],
)
