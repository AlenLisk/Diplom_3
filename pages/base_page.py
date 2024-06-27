import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


from locators import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, delay=5):
        return WebDriverWait(self.driver, delay).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Перейти на сайт')
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step('Получить текущий url')
    def get_current_url(self):
        current_url = self.driver.current_url

        return current_url

    @allure.step('Нажать на кнопку Личный кабинет')
    def click_button_personal_account(self):
        button = self.find_element(BasePageLocators.BUTTON_PERSONAL_ACCOUNT)
        button.click()

    @allure.step('Нажать на кнопку Конструктор')
    def click_button_constructor(self):
        button = self.find_element(BasePageLocators.BUTTON_CONSTRUCTOR)
        button.click()

    @allure.step('Нажать на кнопку Лента заказов')
    def click_button_order_feed(self):
        button = self.find_element(BasePageLocators.BUTTON_ORDER_FEED)
        button.click()

    @allure.step('Ожидание скрытия элемента')
    def wait_invisibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Перетаскивание элемента')
    def drag_an_element(self, source_element, target_element):
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element).move_to_element(target_element).release().perform()