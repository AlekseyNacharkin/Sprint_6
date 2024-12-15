import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:
    base_url = "https://qa-scooter.praktikum-services.ru/"
    # кнопка "Заказать"
    order_button = (By.CSS_SELECTOR, "button[class='Button_Button__ra12g']")
    # кнопка "Статус заказа"
    order_status_button = (By.CSS_SELECTOR, ".Header_Link__1TAG7")
    # кнопка "Яндекс Самокат"
    yandex_scooter_button = (By.CSS_SELECTOR, ".Header_Logo__23yGT")

    def __init__(self, driver):
        self.driver = webdriver.Chrome()

    def click_on_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def click_on_order_status_button(self):
        self.driver.find_element(*self.order_status_button).click()

    def click_on_yandex_scooter_button(self):
        self.driver.find_element(*self.yandex_scooter_button).click()
