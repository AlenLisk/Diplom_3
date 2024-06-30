from locators import *
from pages.base_page import BasePage
import allure


class PersonalAccountPage(BasePage):

    @allure.step('Нажать на кнопку История заказов')
    def click_button_order_history(self):
        self.wail_modal_loading()
        button = self.find_element(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY)
        button.click()

    @allure.step('Найти на странице кнопку История заказов')
    def find_button_order_history(self):
        return self.find_element(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY)

    @allure.step('Нажать на кнопку Выход')
    def click_button_logout(self):
        button = self.find_element(PersonalAccountPageLocators.BUTTON_LOGOUT)
        button.click()
        self.wait_click_element(LoginPageLocators.BUTTON_LOGIN)

    @allure.step('Получить номер последнего заказа в Истории')
    def get_number_last_order(self):
        number = self.find_element(PersonalAccountPageLocators.LAST_ORDER)
        value = number.text

        return value
