from locators import *
from pages.base_page import BasePage
from test_data import UserData
import allure


class ForgotPasswordPage(BasePage):
    @allure.step('Ввести логин в поле ввода')
    def set_email(self):
        field = self.find_element(ForgotPasswordPageLocators.FIELD_EMAIL)
        field.send_keys(UserData.email)
        value = field.get_attribute('value')

        return value

    @allure.step('Нажать на кнопку Восстановить')
    def click_button_restore(self):
        button = self.find_element(ForgotPasswordPageLocators.BUTTON_RESTORE)
        button.click()
        self.wait_click_element(ResetPasswordPageLocators.BUTTON_SAVE)

    @allure.step('Нажйти кнопку восстановить')
    def find_button_restore(self):
        return self.find_element(ForgotPasswordPageLocators.BUTTON_RESTORE)