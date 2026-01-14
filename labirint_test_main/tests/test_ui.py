import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.main_page import BASE_URL
from pages.main_page import BOOK_ID
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.story("Поиск книги")
@allure.title("Проверка поиска книги на главной странице")
def test_search_book(driver):
    main_page = MainPage(driver)
    with allure.step("Открываем главную страницу"):
        main_page.open(BASE_URL)
    with allure.step("Ищем книгу по ID"):
        main_page.search_book(BOOK_ID)
    with allure.step("Проверяем, что результаты поиска содержат книгу"):
        assert BOOK_ID in driver.page_source


@allure.story("Открытие карточки книги")
@allure.title("Проверка открытия карточки книги")
def test_open_book_card(driver):
    main_page = MainPage(driver)

    with allure.step("Открываем главную страницу"):
        main_page.open(BASE_URL)

    with allure.step("Ищем книгу по ID"):
        main_page.search_book(BOOK_ID)

    with allure.step("Открываем карточку книги"):
        main_page.open_book_card(BOOK_ID)

    with allure.step("Проверяем, что открылась страница книги"):
        assert BOOK_ID in driver.current_url


@allure.story("Работа с корзиной")
@allure.title("Проверка добавления книги в корзину")
def test_add_book_to_cart(driver):
    main_page = MainPage(driver)

    with allure.step("Открываем главную страницу"):
        main_page.open(BASE_URL)

    with allure.step("Добавляем книгу в корзину"):
        main_page.add_book_to_cart(BOOK_ID)

    with allure.step("Проверяем, что книга появилась в корзине"):
        assert "Корзина" in driver.page_source


@allure.story("Очистка корзины")
@allure.title("Проверка очистки корзины")
def test_clear_cart(driver):
    main_page = MainPage(driver)

    with allure.step("Открываем главную страницу"):
        main_page.open(BASE_URL)

    with allure.step("Добавляем книгу в корзину"):
        main_page.add_book_to_cart(BOOK_ID)

    with allure.step("Очищаем корзину"):
        main_page.clear_cart()

    with allure.step("Проверяем, что корзина пустая"):
        assert "Ваша корзина пуста" in driver.page_source

@allure.story("Поиск несущетсвующей книги")
@allure.title("Проверка поиска несуществующей книги")
def test_search_nonexistent_book(driver):
    main_page = MainPage(driver)

    with allure.step("Открываем главную страницу"):
        main_page.open(BASE_URL)

    with allure.step("Ищем несуществующую книгу"):
        main_page.search_book("INVALID_BOOK_999")

    with allure.step("Проверяем сообщение об отсутствии результатов"):
        assert "Ничего не найдено" in driver.page_source
