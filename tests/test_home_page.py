from conftest import *
import allure
from urls import Urls


class TestPersonalAccountPage:
    @allure.title('Проверка перехода в конструктор по кнопке Конструктор')
    def test_button_constructor(self, login_page, personal_account_page, driver):
        login_page.wail_modal_loading()
        login_page.login()
        login_page.wail_modal_loading()
        personal_account_page.click_button_personal_account()
        personal_account_page.wail_modal_loading()
        personal_account_page.find_button_order_history()
        personal_account_page.click_button_constructor()
        current_url = personal_account_page.get_current_url()
        home_page = HomePage(driver)
        element = home_page.find_label_assemble_a_burger()

        assert current_url == Urls.HOME
        assert element.is_displayed() == True

    @allure.title('Проверка перехода в ленту заказов по кнопке Лента Заказов')
    def test_button_feed(self, home_page, order_feed_page):
        home_page.wail_modal_loading()
        home_page.find_label_assemble_a_burger()
        home_page.click_button_order_feed()
        home_page.wail_modal_loading()
        home_page.find_label_order_feed()
        current_url = home_page.get_current_url()
        element = order_feed_page.get_counter_day_value()

        assert current_url == Urls.FEED
        assert element != None

    @allure.title('Проверка открытия модального окна')
    def test_open_modal_window(self, home_page):
        home_page.wail_modal_loading()
        home_page.find_label_assemble_a_burger()
        home_page.click_on_ingredient()
        element = home_page.find_modal_window()

        assert element != None

    @allure.title('Проверка закрытия модального окна')
    def test_close_modal_window(self, home_page):
        home_page.wail_modal_loading()
        home_page.find_label_assemble_a_burger()
        home_page.click_on_ingredient()
        element = home_page.find_modal_window()
        home_page.click_button_cross()

        assert element.is_displayed() == False

    @allure.title('Проверка увеличения счетчика ингредиента')
    def test_ingredient_counter(self, home_page):
        home_page.wail_modal_loading()
        home_page.find_label_assemble_a_burger()
        home_page.drag_ingredient()
        counter_value = home_page.get_value_counter()

        assert counter_value == '2'

    @allure.title('Проверка оформления заказа')
    def test_create_order(self, login_page, driver):
        login_page.wail_modal_loading()
        login_page.login()
        home_page = HomePage(driver)
        home_page.create_order()
        element = home_page.find_modal_window_order()

        assert element.is_displayed() == True
