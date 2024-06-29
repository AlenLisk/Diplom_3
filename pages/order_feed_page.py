from locators import OrderFeedPageLocators
from pages.base_page import BasePage
import allure


class OrderFeedPage(BasePage):
    @allure.step('Нажать на последний заказ')
    def click_last_order(self):
        order = self.find_element(OrderFeedPageLocators.LAST_ORDER)
        order.click()

    @allure.step('Найти Состав в модальном окне')
    def find_label_modal_window(self):
        return self.find_element(OrderFeedPageLocators.CONSIST)

    @allure.step('Получить текущее значение счетчика')
    def get_counter_value(self):
        counter = self.find_element(OrderFeedPageLocators.COUNTER_ORDERS)
        value = counter.text

        return value

    @allure.step('Получить текущее значение ежедневного счетчика')
    def get_counter_day_value(self):
        counter = self.find_element(OrderFeedPageLocators.COUNTER_ORDERS_DAY)
        value = counter.text

        return value

    @allure.step('Получаем номер заказа в работе')
    def get_order_in_work(self):
        return self.get_element_text(OrderFeedPageLocators.NUMBER_ORDER_IN_WORK)

    @allure.step('Ищем нужный заказ в ленте заказов')
    def get_order_in_feed(self, number):
        LOCATOR = OrderFeedPageLocators.get_order(number)
        order = self.find_element(LOCATOR)

        return order
