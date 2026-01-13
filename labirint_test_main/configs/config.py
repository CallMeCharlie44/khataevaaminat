import os

BASE_URL = "https://www.labirint.ru"
API_URL = f"{BASE_URL}/api"
BROWSER = os.getenv("BROWSER", "chrome")
TIMEOUT = 10