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
