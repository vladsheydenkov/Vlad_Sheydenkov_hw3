"""
This module provides pytest fixture
"""


import pytest
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "browserVersion": "90.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}



@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Remote(command_executor="http://0.0.0.0:4444/wd/hub", desired_capabilities=capabilities)
    yield driver
    driver.quit()
