from conftest import *
import allure
from urls import Urls


class TestPersonalAccountPage:
    @allure.title('Проверка перехода в личный кабинет по кнопке Личный Кабинет')
    def test_button_personal_account(self, login_page):
        login_page.login()
        login_page.click_button_personal_account()
        current_url = login_page.get_current_url()

        assert current_url == Urls.PERSONAL_ACCOUNT

    @allure.title('Проверка перехода в раздел История заказов')
    def test_button_order_history(self, login_page, personal_account_page):
        login_page.login()
        login_page.click_button_personal_account()
        personal_account_page.click_button_order_history()
        current_url = login_page.get_current_url()

        assert current_url == Urls.ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_button_logout(self, login_page, personal_account_page):
        login_page.login()
        login_page.click_button_personal_account()
        personal_account_page.click_button_logout()
        current_url = login_page.get_current_url()

        assert current_url == Urls.LOGIN
