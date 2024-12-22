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
    user_data = User_Data(driver)
    driver.get(User_Data.order_url)
    user_data.send_keys_to_name_field("Алексей")
    user_data.send_keys_to_surname_field("Начаркин")
    user_data.send_keys_to_adres_field("дом у")
    user_data.send_keys_to_phone_number_field("888888888888")
    #time.sleep(2)
    user_data.choose_metro_station()
    user_data.click_on_accept_user_data_button()
    time.sleep(2)

def test_choose_date_bring_the_scooter(driver):
    scooter_arenda_data = ScooterArendaData(driver)
