import pytest
import allure
from pages.main_page import MainPage
from data.config import BASE_URL  # добавили импорт URL

@pytest.mark.ui
@allure.title("Проверка поиска книги по ID")
def test_search_book(driver):
    main_page = MainPage(driver)
    main_page.open(BASE_URL)
    main_page.search_book("1984")  # можно ввести название книги
    assert "1984" in driver.page_source, "Книга '1984' не найдена на странице"
