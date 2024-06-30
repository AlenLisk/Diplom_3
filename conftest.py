import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.personal_account_page import PersonalAccountPage
from pages.reset_password_page import ResetPasswordPage
from pages.order_feed_page import OrderFeedPage
from pages.home_page import HomePage
from urls import Urls
import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
    else:
        raise ValueError("Браузер не поддерживается")

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
    url = Urls.RESTORE_PASSWORD
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.go_to_site(url)

    return forgot_password_page


@pytest.fixture
def reset_password_page(driver):
    reset_password_page = ResetPasswordPage(driver)

    return reset_password_page


@pytest.fixture
def personal_account_page(driver):
    personal_account_page = PersonalAccountPage(driver)

    return personal_account_page


@pytest.fixture
def home_page(driver):
    url = Urls.HOME
    home_page = HomePage(driver)
    home_page.go_to_site(url)

    return home_page


@pytest.fixture
def order_feed_page(driver):
    order_feed_page = OrderFeedPage(driver)

    return order_feed_page
