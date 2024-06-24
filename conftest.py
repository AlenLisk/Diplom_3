import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from urls import Urls

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    url = Urls.LOGIN
    login_page = LoginPage(driver)
    login_page.go_to_site(url)

    return login_page

@pytest.fixture
def forgot_password_page(driver):
    forgot_password_page = ForgotPasswordPage(driver)

    return forgot_password_page


@pytest.fixture
def order_page(driver):
    order_page = OrderPage(driver)

    return order_page