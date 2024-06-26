from locators import LoginPageLocators
from pages.base_page import BasePage
from test_data import UserData
import allure


class LoginPage(BasePage):
    @allure.step('Нажать на ссылку Восстановить пароль')
    def click_link_forgot_password(self):
        link = self.find_element(LoginPageLocators.LINK_RESTORE_PASSWORD)
        link.click()

    @allure.step('Ввести логин в поле ввода')
    def set_email(self):
        field = self.find_element(LoginPageLocators.FIELD_EMAIL)
        field.send_keys(UserData.email)

    @allure.step('Ввести пароль в поле ввода')
    def set_password(self):
        field = self.find_element(LoginPageLocators.FIELD_PASSWORD)
        field.send_keys(UserData.password)

    @allure.step('Нажать на кнопку Войти')
    def click_button_login(self):
        button = self.find_element(LoginPageLocators.BUTTON_LOGIN)
        button.click()


    @allure.step('Логин')
    def login(self):
        self.set_email()
        self.set_password()
        self.click_button_login()