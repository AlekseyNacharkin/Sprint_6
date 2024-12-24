import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from Sprint_6.pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    base_url = "https://qa-scooter.praktikum-services.ru/"
    # кнопка "Заказать" в середине страницы
    order_button_middle_position = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # кнопка "Сколько это стоит? И как оплатить?"
    button_how_much_does_it_cost_and_how_to_pay = (By.XPATH, ".//div[@id='accordion__heading-0']")
    # Текст псле нажатия на кнопку "Сколько это стоит? И как оплатить?"
    text_assert_button_how_much_does_it_cost_and_how_to_pay = (By.XPATH,".//p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")
    # кнопка "Хочу сразу несколько самокатов! Так можно?"
    button_arend_several_scooters = (By.XPATH, ".//div[@id='accordion__heading-1']")
    # Текст после нажатия на кнопку "Хочу сразу несколько самокатов! Так можно?"
    text_assert_button_arend_several_scooters = (By.XPATH, ".//p[contains(text(), 'Пока что у нас так: один заказ — один самокат')]")
    # кнопка "Как рассчитывается время аренды?"
    button_calculate_arend_time = (By.XPATH, ".//div[@id='accordion__heading-2']")
    # Текст после нажатия на кнопку "Как рассчитывается время аренды?"
    text_button_calculate_arend_time = (By.XPATH, ".//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая')]")
    # кнопка "Можно ли заказать самокат прямо на сегодня?"
    button_order_a_scooter_today = (By.XPATH, ".//div[@id='accordion__heading-3']")
    # Текст после нажатия на кнопку "Можно ли заказать самокат прямо на сегодня?"
    text_button_order_a_scooter_today = (By.XPATH, ".//p[contains(text(), 'Только начиная с завтрашнего дня')]")
    # кнопка "Можно ли продлить заказ или вернуть самокат раньше?"
    button_possible_to_extend_the_order_or_return_the_scooter_earlier = (By.XPATH, ".//div[@id='accordion__heading-4']")
    # Текст после нажатия на кнопку "Можно ли продлить заказ или вернуть самокат раньше?"
    text_button_possible_to_extend_the_order_or_return_the_scooter_earlier = (By.XPATH, ".//p[contains(text(), 'Пока что нет!')]")
    # кнопка "Вы привозите зарядку вместе с самокатом?"
    button_bring_the_charger_with_scooter = (By.XPATH, ".//div[@id='accordion__heading-5']")
    # Текст после нажатия на кнопку "Вы привозите зарядку вместе с самокатом?"
    text_get_text_button_bring_the_charger_with_scooter = (By.XPATH, ".//p[contains(text(), 'Самокат приезжает к вам с полной зарядкой.')]")
    # кнопка "Можно ли отменить заказ?"
    button_cancel_the_order = (By.XPATH, ".//div[@id='accordion__heading-6']")
    # Текст после нажатия на кнопку "Можно ли отменить заказ?"
    text_button_cancel_the_order = (By.XPATH, ".//p[contains(text(), 'Да, пока самокат не привезли')]")
    # кнопка "Я жизу за МКАДом, привезёте?"
    button_info_areal_scooter_arend = (By.XPATH, ".//div[@id='accordion__heading-7']")
    # Текст после нажатия на кнопку "Я жизу за МКАДом, привезёте?"
    text_button_info_areal_scooter_arend = (By.XPATH, ".//p[contains(text(), 'Да, обязательно.')]")
    # Цена аренды
    price_arend = (By.XPATH,".//p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")

    def get_base_url(self):
        self.get_url_page(self.base_url)

    def click_on_order_button_middle_position(self):
        self.click(self.order_button_middle_position)

    def click_on_button_how_much_does_it_cost_and_how_to_pay(self):
        self.click(self.button_how_much_does_it_cost_and_how_to_pay)

    def click_on_button_arend_several_scooters(self):
        self.click(self.button_arend_several_scooters)

    def click_on_button_calculate_arend_time(self):
        self.click(self.button_calculate_arend_time)

    def click_on_button_order_a_scooter_today(self):
        self.click(self.button_order_a_scooter_today)

    def click_on_button_possible_to_extend_the_order_or_return_the_scooter_earlier(self):
        self.click(self.button_possible_to_extend_the_order_or_return_the_scooter_earlier)

    def click_on_button_bring_the_charger_with_scooter(self):
        self.click(self.button_bring_the_charger_with_scooter)

    def click_on_button_cancel_the_order(self):
        self.click(self.button_cancel_the_order)

    def click_on_button_info_areal_scooter_arend(self):
        self.click(self.button_info_areal_scooter_arend)

    def get_text_price_arend(self):
        return self.get_visible_element_text(self.text_assert_button_how_much_does_it_cost_and_how_to_pay)

    def get_text_arend_several_scooters(self):
        return self.get_visible_element_text(self.text_assert_button_arend_several_scooters)

    def get_text_button_calculate_arend_time(self):
        return self.get_visible_element_text(self.text_button_calculate_arend_time)

    def get_text_order_a_scooter_today(self):
        return self.get_visible_element_text(self.text_button_order_a_scooter_today)

    def get_text_button_possible_to_extend_the_order_or_return_the_scooter_earlier(self):
        return self.get_visible_element_text(self.text_button_possible_to_extend_the_order_or_return_the_scooter_earlier)

    def get_text_button_bring_the_charger_with_scooter(self):
        return self.get_visible_element_text(self.text_get_text_button_bring_the_charger_with_scooter)

    def get_text_button_cancel_the_order(self):
        return self.get_visible_element_text(self.text_button_cancel_the_order)

    def get_text_button_info_areal_scooter_arend(self):
        return self.get_visible_element_text(self.text_button_info_areal_scooter_arend)

