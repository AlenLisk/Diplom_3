import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


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
