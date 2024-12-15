import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Order_ScootrPage:
    # поле "Имя"
    name_field = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    # поле "Фамилия"
    surname_field = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    # поле "Адрес: куда привезти заказ"
    adres_field = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    # список "Станция метро"
    metro_station_list = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    # поле "Телефон: на него позвонит курьер"
    phone_number_field = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")

    def __init__(self,driver):
        self.driver = webdriver.Chrome()

    def send_keys_to_name_field(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def send_keys_to_surname_field(self,surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def send_keys_to_adres_field(self,adres):
        self.driver.find_element(*self.adres_field).send_keys(adres)

    def send_keys_to_phone_number_field(self,phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def choose_metro_station(self):
        self.driver.find_element(*self.metro_station_list).click()

