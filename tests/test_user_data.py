import time

from Sprint_6.pages.scoter_arenda_data import ScooterArendaData
from Sprint_6.pages.user_data_page import UserData


class TestUserData:

    def test_filling_in_user_data(self,driver):
        test_user_data = UserData(driver)
        test_user_data.get_url_order_data()
        test_user_data.filling_in_user_data("Алексей", "Начаркин", "дом улица", "8888888888888")
        scooter_arenda_data = ScooterArendaData(driver)
        scooter_arenda_data.filling_arend_date_fields("Оставить у двери")
        time.sleep(2)

    def test_choose_metro_station(self,driver):
        test_user_data = UserData(driver)
        test_user_data.get_url_order_data()
        test_user_data.choose_metro_station_q()
        time.sleep(2)
