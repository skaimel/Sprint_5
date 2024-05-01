from selenium import webdriver
import pytest
from urls import Url


@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.get(Url.main)

    yield driver

    driver.quit()