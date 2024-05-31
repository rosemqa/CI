import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument("--window-size=1920,1080")

    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options=options)
    # driver = webdriver.Remote('http://127.0.0.1:4440/wd/hub', options=firefox_options)
    request.cls.driver = driver
    yield driver
    driver.quit()
