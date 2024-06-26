from conftest import *
import time
import allure
from urls import Urls
from test_data import UserData


class TestForgotPasswordPage:
    @allure.title('Проверка перехода на страницу Забыл пароль')
    def test_go_to_page_forgot_password(self, login_page):
        login_page.click_link_forgot_password()
        current_url = login_page.get_current_url()

        assert current_url == Urls.RESTORE_PASSWORD

    @allure.title('Проверка ввода почты и нажатия кнопки Восстановить')
    def test_set_email_and_click_button_restore(self, forgot_password_page, reset_password_page):
        value = forgot_password_page.set_email()
        forgot_password_page.click_button_restore()
        reset_password_page.find_title_restore_password()
        time.sleep(1)
        current_url = forgot_password_page.get_current_url()

        assert value == UserData.email
        assert current_url == Urls.RESET_PASSWORD

    @allure.title('Проверка подсвечивания поля пароль')
    def test_backlight_field_password(self, forgot_password_page, reset_password_page):
        forgot_password_page.set_email()
        forgot_password_page.click_button_restore()
        reset_password_page.find_title_restore_password()
        reset_password_page.click_button_show_password()
        field = reset_password_page.find_active_field_password()

        assert field != None
