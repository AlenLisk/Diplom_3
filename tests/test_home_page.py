from conftest import *
import time
import allure
from urls import Urls


class TestPersonalAccountPage:
    @allure.title('Проверка перехода в конструктор по кнопке Конструктор')
    def test_button_constructor(self, login_page, personal_account_page):
        login_page.login()
        login_page.click_button_personal_account()
        personal_account_page.find_button_order_history()
        login_page.click_button_constructor()
        current_url = login_page.get_current_url()

        assert current_url == Urls.HOME

    @allure.title('Проверка перехода в ленту заказов по кнопке Лента Заказов')
    def test_button_constructor(self, home_page):
        home_page.find_label_assemble_a_burger()
        home_page.click_button_order_feed()
        home_page.find_label_order_feed()
        current_url = home_page.get_current_url()

        assert current_url == Urls.FEED

    @allure.title('Проверка открытия модального окна')
    def test_open_modal_window(self, home_page):
        home_page.find_label_assemble_a_burger()
        home_page.click_on_ingredient()
        element = home_page.find_modal_window()

        assert element != None

    @allure.title('Проверка закрытия модального окна')
    def test_close_modal_window(self, home_page):
        home_page.find_label_assemble_a_burger()
        home_page.click_on_ingredient()
        element = home_page.find_modal_window()
        home_page.click_button_cross()

        assert element.is_displayed() == False

    @allure.title('Проверка увеличения счетчика ингредиента')
    def test_ingredient_counter(self, home_page):
        home_page.find_label_assemble_a_burger()
        home_page.drag_ingredient()
        counter_value = home_page.get_value_counter()

        assert counter_value == '2'

    @allure.title('Проверка оформления заказа')
    def test_create_order(self, login_page, driver):
        login_page.login()
        home_page = HomePage(driver)
        home_page.find_label_assemble_a_burger()
        home_page.drag_ingredient()
        home_page.click_button_create_order()
        element = home_page.find_modal_window_order()

        assert element.is_displayed() == True




