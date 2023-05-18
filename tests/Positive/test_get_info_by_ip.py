import pytest
import allure
from utils.data_generator import *

@pytest.mark.guest
def test_get_self_ip_inf(ip_api):
    response = ip_api.get_self_ip_information()

    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

    with allure.step("Ответ пришел, посмотрим провайдера"):
        response_body = response.json()
        assert provider in response_body["org"], f"Провайдер определен корректно, получен {response['org']}"


@pytest.mark.guest
def test_get_valid_v4_ip_inf(ip_api):
    response = ip_api.get_some_ip_information(valid_ip_v4)

    with allure.step("Запрос отправлен, проверим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

    with allure.step("Ответ пришел, проверим тело ответа"):
        response_body = response.json()
        assert company_valid_ip_v4 in response_body["org"], "IP не принадлежит ожидаемой компании"


@pytest.mark.guest
def test_get_valid_v6_ip_inf(ip_api):
    response = ip_api.get_some_ip_information(valid_ip_v6)

    with allure.step("Запрос отправлен, проверим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

    with allure.step("Ответ пришел, проверим тело ответа"):
        response_body = response.json()
        assert company_valid_ip_v6 in response_body["org"], "IP не принадлежит ожидаемой компании"