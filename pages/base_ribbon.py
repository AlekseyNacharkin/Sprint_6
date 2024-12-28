from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from pages.base_page import BasePage


class BaseRibbon(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    base_url = "https://qa-scooter.praktikum-services.ru/"
    # кнопка "Заказать" в верхнем риббоне
    order_button_top_position = (By.CSS_SELECTOR, "button[class='Button_Button__ra12g']")
    # кнопка "Статус заказа"
    order_status_button = (By.CSS_SELECTOR, ".Header_Link__1TAG7")
    # Поле "Введите номер заказа"
    field_input_order_number = (By.XPATH, "input[placeholder='Введите номер заказа']")
    # Кнопка "Go!" для поиска номера заказа
    button_accept_order_number = (By.XPATH, "//button[normalize-space()='Go!']")
    # кнопка "Самокат"
    yandex_scooter_button = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    # кнопка "Яндекс"
    yandex_searching_button = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")

    def get_url_base_ribbon(self):
        self.get_url_page(self.base_url)

    def click_on_order_button_top_position(self):
        self.click(self.order_button_top_position)

    def click_on_order_status_button(self):
        self.click(self.order_status_button)

    def click_on_yandex_scooter_button(self):
        self.click(self.yandex_scooter_button)

    def click_on_yandex_dzen(self):
        self.click(self.yandex_searching_button)


