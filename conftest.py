import pytest
from dotenv import dotenv_values
import requests


class IpApiClient:
    def __init__(self, host, token):
        self.HOST = host
        self.auth_token = token

    def __str__(self):
        return f"HOST is {self.HOST} and auth_token is {self.auth_token}"

    def get_self_ip_information(self, path='/', params=None, headers=None):
        url = f'{self.HOST}{path}'
        return requests.get(url=url, params=params, headers=headers)

    def get_some_ip_information(self, ip: str, path='/', params=None, headers=None):
        url = f'{self.HOST}{path}{ip}'
        return requests.get(url=url, params=params, headers=headers)


@pytest.fixture
def ip_api():
    env_dict = dotenv_values()
    return IpApiClient(env_dict["API_HOST"], env_dict["AUTH_TOKEN"])





