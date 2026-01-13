import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # или другой браузер, который у тебя установлен
    driver.maximize_window()
    yield driver
    driver.quit()