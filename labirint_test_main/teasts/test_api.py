import pytest
import requests
import allure

API_URL = "https://reqres.in/api"

@pytest.mark.api
@allure.title("Проверка получения информации о пользователе")
def test_get_user():
    with allure.step("Делаем GET-запрос к API пользователя"):
        response = requests.get(f"{API_URL}/users/2")
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200

@pytest.mark.api
@allure.title("Проверка получения списка пользователей")
def test_list_users():
    with allure.step("Делаем GET-запрос списка пользователей"):
        response = requests.get(f"{API_URL}/users?page=2")
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200
    with allure.step("Проверяем, что возвращается список"):
        assert "data" in response.json()