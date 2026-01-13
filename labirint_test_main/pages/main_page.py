# pages/main_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure

class MainPage:
    SEARCH_FIELD = (By.ID, "search-field")  # Поле поиска на главной
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")  # Кнопка "Найти"

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
