import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:

    # кнопка "Заказать" в середине страницы
    order_button_middle_position = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # кнопка "Сколько это стоит? И как оплатить?"
    button_how_much_does_it_cost_and_how_to_pay = (By.XPATH, ".//div[@id='accordion__heading-0']")
    # кнопка "Хочу сразу несколько самокатов! Так можно?"
    button_arend_several_scooters = (By.XPATH, ".//div[@id='accordion__heading-1']")
    # кнопка "Как рассчитывается время аренды?"
    button_calculate_arend_time = (By.XPATH, ".//div[@id='accordion__heading-2']")
    # кнопка "Можно ли заказать самокат прямо на сегодня?"
    button_order_a_scooter_today = (By.XPATH, ".//div[@id='accordion__heading-3']")
    # кнопка "Можно ли продлить заказ или вернуть самокат раньше?"
    button_possible_to_extend_the_order_or_return_the_scooter_earlier = (By.XPATH, ".//div[@id='accordion__heading-4']")
    # кнопка "Вы привозите зарядку вместе с самокатом?"
    button_bring_the_charger_with_scooter = (By.XPATH, ".//div[@id='accordion__heading-5']")
    # кнопка "Можно ли отменить заказ?"
    button_cancel_the_order = (By.XPATH, ".//div[@id='accordion__heading-6']")
    # кнопка "Я жизу за МКАДом, привезёте?"
    button_info_areal_scooter_arend = (By.XPATH, ".//div[@id='accordion__heading-7']")

    def __init__(self, driver):
        self.driver = webdriver.Chrome()

    def click_on_order_button_middle_position(self):
        self.driver.find_element(*self.order_button_middle_position).click()

    def click_on_button_how_much_does_it_cost_and_how_to_pay(self):
        self.driver.find_element(*self.button_how_much_does_it_cost_and_how_to_pay).click()

    def click_on_button_arend_several_scooters(self):
        self.driver.find_element(*self.button_arend_several_scooters).click()

    def click_on_button_calculate_arend_time(self):
        self.driver.find_element(*self.button_calculate_arend_time).click()

    def click_on_button_order_a_scooter_today(self):
        self.driver.find_element(*self.button_order_a_scooter_today).click()

    def click_on_button_possible_to_extend_the_order_or_return_the_scooter_earlier(self):
        self.driver.find_element(*self.button_possible_to_extend_the_order_or_return_the_scooter_earlier).click()

    def click_on_button_bring_the_charger_with_scooter(self):
        self.driver.find_element(*self.button_bring_the_charger_with_scooter).click()

    def click_on_button_cancel_the_order(self):
        self.driver.find_element(*self.button_cancel_the_order).click()

    def click_on_button_info_areal_scooter_arend(self):
        self.driver.find_element(*self.button_info_areal_scooter_arend).click()

