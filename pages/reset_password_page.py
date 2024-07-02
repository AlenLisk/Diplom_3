from locators import ResetPasswordPageLocators
from pages.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):
    @allure.step('Нажать на кнопку Показать пароль')
    def click_button_show_password(self):
        button = self.find_element(ResetPasswordPageLocators.BUTTON_SHOW_PASSWORD)
        button.click()


    @allure.step('Поиск активного поля Пароль')
    def find_active_field_password(self):
        field = self.find_element(ResetPasswordPageLocators.INPUT_STATUS_ACTIVE)

        return field

    @allure.step('Поиск заголловка Восстановление пароля')
    def find_title_restore_password(self):
        return self.find_element(ResetPasswordPageLocators.TITLE_RESTORE_PASSWORD)
