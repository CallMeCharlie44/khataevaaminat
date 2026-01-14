import pytest
import requests
import allure
from pages.main_page import USER_EMAIL, USER_PASSWORD

API_URL = "https://reqres.in/api"


@allure.story("Получение данных пользователя")
@pytest.mark.api
@allure.title("Проверка получения информации о пользователе")
def test_get_user():
    with allure.step("Делаем GET-запрос к API пользователя"):
        response = requests.get(f"{API_URL}/users/2")
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200


@allure.story("Получение списка пользователей")
@pytest.mark.api
@allure.title("Проверка получения списка пользователей")
def test_list_users():
    with allure.step("Делаем GET-запрос списка пользователей"):
        response = requests.get(f"{API_URL}/users?page=2")
    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200
    with allure.step("Проверяем, что возвращается список"):
        assert "data" in response.json()


@allure.story("Создание пользователя")
@pytest.mark.api
@allure.title("Проверка создания пользователя")
def test_create_user():
    payload = {"name": "John", "job": "QA Engineer"}

    with allure.step("Отправляем POST-запрос на создание пользователя"):
        response = requests.post(f"{API_URL}/users", json=payload)

    with allure.step("Проверяем статус-код 201"):
        assert response.status_code == 201

    with allure.step("Проверяем, что пользователь создан"):
        response_json = response.json()
        assert response_json["name"] == payload["name"]
        assert response_json["job"] == payload["job"]
        assert "id" in response_json
        assert "createdAt" in response_json


@allure.story("Обновление пользователя")
@pytest.mark.api
@allure.title("Проверка обновления данных пользователя")
def test_update_user():
    payload = {"name": "Jane", "job": "Senior QA"}

    with allure.step("Отправляем PUT-запрос на обновление пользователя"):
        response = requests.put(f"{API_URL}/users/2", json=payload)

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверяем, что данные пользователя обновлены"):
        response_json = response.json()
        assert response_json["name"] == payload["name"]
        assert response_json["job"] == payload["job"]
        assert "updatedAt" in response_json

@allure.story("Авторизация без пароля")
@pytest.mark.api
@allure.title("Проверка ошибки авторизации без пароля")
def test_login_without_password():
    payload = {"email": "eve.holt@reqres.in"}
    with allure.step("Отправляем POST-запрос без пароля"):
        response = requests.post(f"{API_URL}/login", json=payload)

    with allure.step("Проверяем статус-код 400"):
        assert response.status_code == 400

    with allure.step("Проверяем текст ошибки"):
        assert response.json()["error"] == "Missing password"
