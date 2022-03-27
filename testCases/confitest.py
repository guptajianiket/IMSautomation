from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup():
    service = Service("C:\\Users\\aniket.gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    return driver

