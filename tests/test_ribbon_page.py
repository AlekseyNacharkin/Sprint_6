import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium import webdriver
from Sprint_6.pages.base_ribbon import BaseRibbon
from Sprint_6.pages.user_data_page import User_Data

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_click_on_order_button_top_position(driver):
    base_ribbon = BaseRibbon(driver)
    driver.get(BaseRibbon.base_url)
    base_ribbon.click_on_order_button_top_position()

def test_choose_metro_station_q(driver):
    order_scooter_page = User_Data(driver)
    driver.get(User_Data.order_url)
    order_scooter_page.choose_metro_station_q()
    time.sleep(2)