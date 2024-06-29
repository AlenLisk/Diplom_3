from locators import PersonalAccountPageLocators
from pages.base_page import BasePage
import allure
import time


class PersonalAccountPage(BasePage):

    @allure.step('Нажать на кнопку История заказов')
    def click_button_order_history(self):
        button = self.find_element(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY)
        button.click()

    @allure.step('Найти на странице кнопку История заказов')
    def find_button_order_history(self):
        return self.find_element(PersonalAccountPageLocators.BUTTON_ORDER_HISTORY)

    @allure.step('Нажать на кнопку Выход')
    def click_button_logout(self):
        button = self.find_element(PersonalAccountPageLocators.BUTTON_LOGOUT)
        button.click()

    @allure.step('Получить номер последнего заказа в Истории')
    def get_number_last_order(self):
        number = self.find_element(PersonalAccountPageLocators.LAST_ORDER)
        value = number.text

        return value

