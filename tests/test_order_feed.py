from conftest import *
import allure
from urls import Urls


class TestOrderFeedPage:
    @allure.title('Проверка окна с деталями заказа')
    def test_order_details_modal_window(self, login_page, order_feed_page):
        login_page.login()
        login_page.click_button_order_feed()
        order_feed_page.click_last_order()
        element = order_feed_page.find_label_modal_window()

        assert element != None

    @allure.title('Проверка счетчика заказов')
    def test_orders_counter(self, login_page, driver, order_feed_page):
        login_page.login()
        login_page.click_button_order_feed()
        old_value = order_feed_page.get_counter_value()
        order_feed_page.click_button_constructor()
        home_page = HomePage(driver)
        home_page.create_order_modification()
        home_page.click_button_order_feed()
        new_value = order_feed_page.get_counter_value()

        assert int(old_value) < int(new_value)

    @allure.title('Проверка ежедневного счетчика заказов')
    def test_orders_day_counter(self, login_page, driver, order_feed_page):
        login_page.login()
        login_page.click_button_order_feed()
        old_value = order_feed_page.get_counter_day_value()
        order_feed_page.click_button_constructor()
        home_page = HomePage(driver)
        home_page.create_order_modification()
        home_page.click_button_order_feed()
        new_value = order_feed_page.get_counter_day_value()

        assert int(old_value) < int(new_value)

    @allure.title('Проверка есть ли заказ в работе')
    def test_order_in_work(self, login_page, driver, order_feed_page):
        login_page.login()
        home_page = HomePage(driver)
        order_number = home_page.create_order_modification()
        home_page.click_button_order_feed()
        order_number_in_work = order_feed_page.get_order_in_work()

        assert '0' + order_number == order_number_in_work

    @allure.title('Проверка отображения заказов в Лента заказов')
    def test_display_orders(self, login_page, driver, personal_account_page):
        login_page.login()
        home_page = HomePage(driver)
        order_number = home_page.create_order_modification()
        login_page.click_button_personal_account()
        personal_account_page.click_button_order_history()
        order_number_in_order_history = personal_account_page.get_number_last_order()
        personal_account_page.go_to_site(Urls.FEED)
        order_feed_page = OrderFeedPage(driver)
        order_number_in_feed = order_feed_page.get_order_in_feed(order_number_in_order_history)

        assert '#0' + order_number == order_number_in_order_history
        assert order_number_in_feed != None
