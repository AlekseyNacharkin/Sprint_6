import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from Sprint_6.pages.base_page import BasePage

class ScooterArendaData(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # Поле "Когда привезти самокат"
    date_bring_the_scooter_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    #кнопки выбора даты заказа самоката
    date_buttons = (By.XPATH, ".//div[@role='button']")
    # Поле выбора "Срок аренды"
    rental_period_field = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    # Кнопки выбора срока аренды
    rental_period_date_buttons = (By.XPATH, "//div[@class='Dropdown-option']")
    # Цвет самоката "черный жемчуг"
    black_color_scooter = (By.XPATH, ".//input[@id='black']")
    # Цвет самоката "серая безысходность"
    gray_color_scooter = (By.XPATH, ".//input[@id='grey']")
    # Поле "Комментарий для курьера".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']
    comment_for_courier_field = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']")
    # Кнопка "Назад"
    previous_page_button = (By.XPATH, ".//button[contains(text(),'Назад')]")
    # Кнопка "Заказать"
    accept_order_scooter_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # Кнопка "Да" в окне "Хотите оформить заказ"
    confirm_accept_order_scooter_button = (By.XPATH, ".//button[contains(text(),'Да')]")
    # Кнопка "Нет" в окне "Хотите оформить заказ"
    cancel_accept_order_scooter_button = (By.XPATH, ".//button[contains(text(),'Нет')]")
    # Окно информации о заказе
    window_information_about_order = (By.XPATH, ".//div[@class='Order_Text__2broi']")
    # Кнопка "Посмотреть статус"
    button_view_the_status = (By.XPATH, ".//button[contains(text(),'Посмотреть статус')]")
    # Поле с номером заказа (например 166020)
    number_order_button = (By.XPATH, ".//input[@class='Input_Input__1iN_Z Track_Input__1g7lq Input_Filled__1rDxs Input_Responsible__1jDKN']")