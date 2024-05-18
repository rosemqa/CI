import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
