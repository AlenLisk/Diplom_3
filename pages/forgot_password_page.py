from locators.login_page_locators import LoginPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
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

    @allure.step('Нажать на кнопку Показать пароль')
    def click_button_show_password(self):
        button = self.find_element(ForgotPasswordPageLocators.BUTTON_SHOW_PASSWORD)
        button.click()

    @allure.step('Поиск заголовка Восстановление пароля')
    def find_title_restore_password(self):
        self.find_element(ForgotPasswordPageLocators.TITLE_RESTORE_PASSWORD)

    @allure.step('Поиск активного поля Пароль')
    def find_active_field_password(self):
        field = self.find_element(ForgotPasswordPageLocators.INPUT_STATUS_ACTIVE)

        return field
