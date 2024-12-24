import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium import webdriver
from Sprint_6.pages.base_ribbon import BaseRibbon
from Sprint_6.pages.user_data_page import UserData
from Sprint_6.pages.start_page import StartPage

class TestQuestion():

    def test_question_about_pay(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_how_much_does_it_cost_and_how_to_pay()
        text = start_page.get_text_price_arend()
        assert text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_question_arend_several_scooters(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_arend_several_scooters()
        text = start_page.get_text_arend_several_scooters()
        assert text == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    def test_question_button_calculate_arend_time(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_calculate_arend_time()
        text = start_page.get_text_button_calculate_arend_time()
        assert text == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def test_question_order_a_scooter_today(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_order_a_scooter_today()
        text = start_page.get_text_order_a_scooter_today()
        assert text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_question_possible_to_extend_the_order_or_return_the_scooter_earlier(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_possible_to_extend_the_order_or_return_the_scooter_earlier()
        text = start_page.get_text_button_possible_to_extend_the_order_or_return_the_scooter_earlier()
        assert text == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    def test_question_button_bring_the_charger_with_scooter(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_bring_the_charger_with_scooter()
        text = start_page.get_text_button_bring_the_charger_with_scooter()
        assert text == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    def test_question_button_cancel_the_order(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_cancel_the_order()
        text = start_page.get_text_button_cancel_the_order()
        assert text == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    def test_question_button_info_areal_scooter_arend(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_info_areal_scooter_arend()
        text = start_page.get_text_button_info_areal_scooter_arend()
        assert text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
