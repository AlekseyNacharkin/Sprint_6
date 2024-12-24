import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium import webdriver
from Sprint_6.pages.base_ribbon import BaseRibbon
from Sprint_6.pages.user_data_page import UserData

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()