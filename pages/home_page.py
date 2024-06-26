from locators import *
from pages.base_page import BasePage
import allure


class HomePage(BasePage):
    @allure.step('Найти заголовок Соберите бургер')
    def find_label_assemble_a_burger(self):
        return self.find_element(HomePageLocators.LABEL_ASSEMBLE_A_BURGER)

    @allure.step('Найти заголовок Лента заказов')
    def find_label_order_feed(self):
        return self.find_element(HomePageLocators.LABEL_ORDER_FEED)
