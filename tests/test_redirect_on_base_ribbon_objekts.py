import time
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Redirect_URLS
from pages.base_ribbon import BaseRibbon
from pages.scoter_arenda_data import ScooterArendaData
from pages.user_data_page import UserData
from pages.start_page import StartPage

class TestRedirectRibbonObjekts():

    @allure.title("Тест редиректа на стартовую страницу заказа самоката")
    def test_redirect_on_scooter_start_page(self,driver):
        user_data_page = UserData(driver)
        user_data_page.get_url_order_data()
        base_ribbon = BaseRibbon(driver)
        base_ribbon.click_on_yandex_scooter_button()
        assert driver.current_url == base_ribbon.base_url

    @allure.title("Тест редиректа на страницу яндекс дзен")
    def test_redirect_on_dzen_page(self,driver):
        user_data_page = UserData(driver)
        user_data_page.get_url_order_data()
        base_ribbon = BaseRibbon(driver)
        base_ribbon.click_on_yandex_dzen()
        base_ribbon.switch_to_new_tab()
        base_ribbon.waiting_load_url(Redirect_URLS.REDIRECT_DZEN_URL)
        assert driver.current_url == Redirect_URLS.REDIRECT_DZEN_URL
