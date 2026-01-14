from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import allure
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://www.labirint.ru"
API_URL = f"{BASE_URL}/api"
BROWSER = os.getenv("BROWSER", "chrome")
TIMEOUT = 10
BOOK_ID = "662723"
USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")


class MainPage:
    SEARCH_FIELD = (By.ID, "search-field")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем сайт Лабиринт")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ищем книгу по названию или автору")
    def search_book(self, text):
        field = self.driver.find_element(*self.SEARCH_FIELD)
        field.clear()
        field.send_keys(text)
        field.send_keys(Keys.ENTER)

    @allure.step("Открываем карточку первой книги")
    def open_book_card(self):
        self.driver.find_element(*self.BOOK_CARD).click()

    @allure.step("Добавляем книгу в корзину")
    def add_book_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
        time.sleep(2)

    @allure.step("Открываем корзину")
    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    @allure.step("Очищаем корзину")
    def clear_cart(self):
        self.open_cart()
        self.driver.find_element(*self.CLEAR_CART_BUTTON).click()
        time.sleep(2)
