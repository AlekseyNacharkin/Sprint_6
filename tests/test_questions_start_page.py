import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium import webdriver

from constants import *
from pages.start_page import StartPage


class TestQuestion():

    @allure.title("Тест текста вопроса 'Сколько это стоит? И как оплатить?'")
    def test_question_about_pay_and_cost(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_how_much_does_it_cost_and_how_to_pay()
        text = start_page.get_text_price_arend()
        assert text == TestQuestions.ASSERTION_TEXT_TEST_QUESTION_ABOUT_PAY_AND_COST

    @allure.title("Тест текста вопроса 'Хочу сразу несколько самокатов! Так можно?'")
    def test_question_arend_several_scooters(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_arend_several_scooters()
        text = start_page.get_text_arend_several_scooters()
        assert text == TestQuestions.ASSERTION_TEXT_TEST_QUESTIONS_AREND_SEVERAL_SCOOTERS

    @allure.title("Тест текста вопроса 'Как рассчитывается время аренды?'")
    def test_question_button_calculate_arend_time(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_calculate_arend_time()
        text = start_page.get_text_button_calculate_arend_time()
        assert text == TestQuestions.ASSERTION_TEXT_TEST_QUESTION_BUTTON_CALCULATE_AREND_TIME

    @allure.title("Тест текста вопроса 'Можно ли заказать самокат прямо на сегодня?'")
    def test_question_order_a_scooter_today(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_order_a_scooter_today()
        text = start_page.get_text_order_a_scooter_today()
        assert text == TestQuestions.ASSERTION_TEXT_TEST_QUESTION_ORDER_A_SCOOTER_TODAY

    @allure.title("Тест текста вопроса 'Можно ли продлить заказ или вернуть самокат раньше?'")
    def test_question_possible_to_extend_the_order_or_return_the_scooter_earlier(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_possible_to_extend_the_order_or_return_the_scooter_earlier()
        text = start_page.get_text_button_possible_to_extend_the_order_or_return_the_scooter_earlier()
        assert text == TestQuestions.ASSERTION_TEXT_TEST_QUESTION_POSSIBLE_TO_EXTEND_THE_ORDER

    @allure.title("Тест текста вопроса 'Вы привозите зарядку вместе с самокатом?'")
    def test_question_button_bring_the_charger_with_scooter(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_bring_the_charger_with_scooter()
        text = start_page.get_text_button_bring_the_charger_with_scooter()
        assert text == TestQuestions.ASSERTION_TEXT_TEST_QUESTION_BUTTON_BRING_THE_CHARGER_WITH_SCOOTER

    @allure.title("Тест текста вопроса 'Можно ли отменить заказ?'")
    def test_question_button_cancel_the_order(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_cancel_the_order()
        text = start_page.get_text_button_cancel_the_order()
        assert text == TestQuestions.ASSERTION_TEXT_TEST_QUESTION_BUTTON_CANCEL_THE_ORDER

    @allure.title("Тест текста вопроса 'Я жизу за МКАДом, привезёте?'")
    def test_question_button_info_areal_scooter_arend(self,driver):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.click_on_button_info_areal_scooter_arend()
        text = start_page.get_text_button_info_areal_scooter_arend()
        assert text == TestQuestions.ASSERTION_TEXT_TEST_QUESTION_BUTTONS_INFO_AREAL_SCOOTER_AREND
