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

TEST_QUESTIONS_DATA = [
    {
        "click": StartPage.click_on_button_how_much_does_it_cost_and_how_to_pay,
        "get_text": StartPage.get_text_price_arend,
        "expected_text": TestQuestions.ASSERTION_TEXT_TEST_QUESTION_ABOUT_PAY_AND_COST,
    },
    {
        "click": StartPage.click_on_button_arend_several_scooters,
        "get_text": StartPage.get_text_arend_several_scooters,
        "expected_text": TestQuestions.ASSERTION_TEXT_TEST_QUESTIONS_AREND_SEVERAL_SCOOTERS,
    },
    {
        "click": StartPage.click_on_button_calculate_arend_time,
        "get_text": StartPage.get_text_button_calculate_arend_time,
        "expected_text": TestQuestions.ASSERTION_TEXT_TEST_QUESTION_BUTTON_CALCULATE_AREND_TIME,
    },
    {
        "click": StartPage.click_on_button_order_a_scooter_today,
        "get_text": StartPage.get_text_order_a_scooter_today,
        "expected_text": TestQuestions.ASSERTION_TEXT_TEST_QUESTION_ORDER_A_SCOOTER_TODAY,
    },
    {
        "click": StartPage.click_on_button_possible_to_extend_the_order_or_return_the_scooter_earlier,
        "get_text": StartPage.get_text_button_possible_to_extend_the_order_or_return_the_scooter_earlier,
        "expected_text": TestQuestions.ASSERTION_TEXT_TEST_QUESTION_POSSIBLE_TO_EXTEND_THE_ORDER
    },
    {
        "click": StartPage.click_on_button_bring_the_charger_with_scooter,
        "get_text": StartPage.get_text_button_bring_the_charger_with_scooter,
        "expected_text": TestQuestions.ASSERTION_TEXT_TEST_QUESTION_BUTTON_BRING_THE_CHARGER_WITH_SCOOTER
    },
    {
        "click": StartPage.click_on_button_cancel_the_order,
        "get_text": StartPage.get_text_button_cancel_the_order,
        "expected_text": TestQuestions.ASSERTION_TEXT_TEST_QUESTION_BUTTON_CANCEL_THE_ORDER
    },
    {
        "click": StartPage.click_on_button_info_areal_scooter_arend,
        "get_text": StartPage.get_text_button_info_areal_scooter_arend,
        "expected_text": TestQuestions.ASSERTION_TEXT_TEST_QUESTION_BUTTONS_INFO_AREAL_SCOOTER_AREND
    }]


class TestQuestion():

    @allure.title("Тест текстов вопроса")
    @pytest.mark.parametrize("data", TEST_QUESTIONS_DATA)
    def test_questions(self, driver, data):
        start_page = StartPage(driver)
        start_page.get_base_url()
        data["click"](start_page)
        actual_text = data["get_text"](start_page)
        assert actual_text == data["expected_text"]

