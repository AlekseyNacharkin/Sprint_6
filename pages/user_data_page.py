import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from Sprint_6.pages.base_page import BasePage


class UserData(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    order_url = "https://qa-scooter.praktikum-services.ru/order"
    # поле "Имя"
    name_field = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    # поле "Фамилия"
    surname_field = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    # поле "Адрес: куда привезти заказ"
    address_field = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    # список "Станция метро"
    metro_station_field = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    #station_locator = (By.XPATH, f".//div[@class='Order_Text__2broi' and contains(text(),'{station_name}')]/parent::button")
    metro_station = (By.XPATH, ".//div[@class='Order_Text__2broi' and contains(text(),'Сокольники')]/parent::button")
    # поле "Телефон: на него позвонит курьер"
    phone_number_field = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка "Далее"
    accept_user_data_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    def get_url_order_data(self):
        self.get_url_page(self.order_url)

    def send_keys_to_name_field(self, name):
        self.send_keys(self.name_field, name)

    def send_keys_to_surname_field(self, surname):
        self.send_keys(self.surname_field, surname)

    def send_keys_to_address_field(self, address):
        self.send_keys(self.address_field, address)

    def send_keys_to_phone_number_field(self, phone_number):
        self.send_keys(self.phone_number_field, phone_number)

    def choose_metro_station(self):
        self.visibility_element(self.metro_station_field)
        self.click_on_scrollbar(self.metro_station_field)
        self.visibility_element(self.metro_station)
        self.click_on_scrollbar(self.metro_station)

    def choose_metro_station_q(self, station_name="Сокольники"):
        self.find_element(self.metro_station_field).click()
        station_locator = (
        By.XPATH, f".//div[@class='Order_Text__2broi' and contains(text(),'{station_name}')]/parent::button")
        self.find_element(station_locator).click()

    def click_on_accept_user_data_button(self):
        self.click(self.accept_user_data_button)

    def filling_in_user_data(self, name, surname, address, phone_number):
        self.send_keys_to_name_field(name)
        self.send_keys_to_surname_field(surname)
        self.send_keys_to_address_field(address)
        self.choose_metro_station()
        self.send_keys_to_phone_number_field(phone_number)
        self.click_on_accept_user_data_button()


