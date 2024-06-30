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

    @allure.step('Найти модальное окно')
    def find_modal_window(self):
        return self.find_element(HomePageLocators.MODAL_WINDOW)

    @allure.step('Нажать на ингредиент')
    def click_on_ingredient(self):
        ingredient = self.find_element(HomePageLocators.INGREDIENT)
        ingredient.click()

    @allure.step('Закрыть модальное окно')
    def click_button_cross(self):
        button = self.find_element(HomePageLocators.CROSS)
        button.click()
        self.wait_invisibility_element(HomePageLocators.MODAL_WINDOW)


    @allure.step('Перетащить ингредиент')
    def drag_ingredient(self):
        source = self.wait_click_element(HomePageLocators.INGREDIENT)
        target = self.wait_click_element(HomePageLocators.ORDER_GENERATOR)
        self.drag_an_element(source, target)

    @allure.step('Получить значение счетчика')
    def get_value_counter(self):
        counter = self.find_element(HomePageLocators.COUNTER)
        value = counter.text

        return value

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_button_create_order(self):
        button = self.find_element(HomePageLocators.BUTTON_CREATE_ORDER)
        button.click()

    @allure.step('Найти модальное окно заказа')
    def find_modal_window_order(self):
        return self.find_element(HomePageLocators.LABEL_ORDER)

    @allure.step('Закрыть модальное окно заказа')
    def click_button_cross_order(self):
        button = self.find_element(HomePageLocators.CROSS)
        button.click()
        self.wait_invisibility_element(HomePageLocators.CROSS)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        number = self.find_element(HomePageLocators.NUMBER_ORDER)
        value = number.text

        return value

    @allure.step('Созать заказ без получения номера и закрытия модального окна')
    def create_order(self):
        self.find_label_assemble_a_burger()
        self.drag_ingredient()
        self.click_button_create_order()

    @allure.step('Созать заказ с получение номера и закрытием модального окна')
    def create_order_modification(self):
        self.find_label_assemble_a_burger()
        self.drag_ingredient()
        self.click_button_create_order()
        self.wail_modal_loading()
        self.wait_click_element(HomePageLocators.CROSS)
        value = self.get_order_number()
        self.click_button_cross_order()
        self.wait_invisibility_element(HomePageLocators.CROSS)

        return value
