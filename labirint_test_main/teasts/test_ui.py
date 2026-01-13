import pytest
from selenium import webdriver
from pages.main_page import MainPage
from data.config import BASE_URL
from data.test_data import BOOK_ID
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Проверка поиска книги на главной странице")
def test_search_book(driver):
    main_page = MainPage(driver)
    with allure.step("Открываем главную страницу"):
        main_page.open(BASE_URL)
    with allure.step("Ищем книгу по ID"):
        main_page.search_book(BOOK_ID)
    with allure.step("Проверяем, что результаты поиска содержат книгу"):
        assert BOOK_ID in driver.page_source