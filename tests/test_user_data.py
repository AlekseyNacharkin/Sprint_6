import time
import allure
import pytest

from pages.base_ribbon import BaseRibbon
from pages.scoter_arenda_data import ScooterArendaData
from pages.user_data_page import UserData
from pages.start_page import StartPage


class TestUserData:

    @allure.title("Тест заполнения данных с кнопки 'Заказать' в рибоне")
    @pytest.mark.parametrize("name, surname, address, phone_number,comment",[("Алексей", "Начаркин", "дом улица", "8888888888888", "Оставить у двери"),
                                                                             ("Зубенко", "Михаил", "улица дом", "8888888888888","Новый коммент")])
    def test_filling_in_user_data_from_ribbon_page(self,driver,name, surname, address, phone_number,comment):
        base_ribbon = BaseRibbon(driver)
        base_ribbon.get_url_base_ribbon()
        base_ribbon.click_on_order_button_top_position()
        test_user_data = UserData(driver)
        test_user_data.filling_in_user_data(name, surname, address, phone_number)
        scooter_arenda_data = ScooterArendaData(driver)
        scooter_arenda_data.filling_arend_date_fields(comment)
        assert scooter_arenda_data.is_displayed(scooter_arenda_data.button_view_the_status)


    @allure.title("Тест заполнения данных с кнопки 'Заказать' со стартовой страницы")
    @pytest.mark.parametrize("name, surname, address, phone_number,comment",
                             [("Алексей", "Начаркин", "дом улица", "8888888888888", "Оставить у двери"),
                              ("Зубенко", "Михаил", "улица дом", "8888888888888", "Новый коммент")])
    def test_filling_in_user_data_from_start_page(self,driver,name, surname, address, phone_number,comment):
        start_page = StartPage(driver)
        start_page.get_base_url()
        start_page.scroll_to_down()
        start_page.click_on_order_button_middle_position()
        test_user_data = UserData(driver)
        test_user_data.filling_in_user_data(name, surname, address, phone_number)
        scooter_arenda_data = ScooterArendaData(driver)
        scooter_arenda_data.filling_arend_date_fields(comment)
        assert scooter_arenda_data.is_displayed(scooter_arenda_data.button_view_the_status)

