from locators.login_page_locators import LoginPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from test_data import UserData
import allure


class LoginPage(BasePage):
    @allure.step('Нажать на ссылку Забыл пароль')
    def click_link_forgot_password(self):
        link = self.find_element(LoginPageLocators.LINK_FORGOT_PASSWORD)
        link.click()

