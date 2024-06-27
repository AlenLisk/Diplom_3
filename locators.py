from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    FIELD_EMAIL = (By.NAME, 'name')
    BUTTON_RESTORE = (By.XPATH, ".//button[text()='Восстановить']")


class ResetPasswordPageLocators:
    BUTTON_SHOW_PASSWORD = (By.XPATH, '//div[contains(@class,"icon-action")]')
    TITLE_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    INPUT_STATUS_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'


class LoginPageLocators:
    LINK_RESTORE_PASSWORD = (By.LINK_TEXT, "Восстановить пароль")
    FIELD_EMAIL = (By.NAME, 'name')
    FIELD_PASSWORD = (By.NAME, 'Пароль')
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")

class PersonalAccountPageLocators:
    BUTTON_ORDER_HISTORY = (By.LINK_TEXT, "История заказов")
    BUTTON_LOGOUT = (By.XPATH, ".//main//button[text()='Выход']")

class BasePageLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//header//p[text()='Личный Кабинет']")
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//header//p[text()='Конструктор']")
    BUTTON_ORDER_FEED = (By.LINK_TEXT, "Лента Заказов")

class HomePageLocators:
    LABEL_ASSEMBLE_A_BURGER = (By.XPATH, ".//main//h1[text()='Соберите бургер']")
    LABEL_ORDER_FEED = (By.XPATH, ".//main//h1[text()='Лента заказов']")
    MODAL_WINDOW = (By.XPATH, ".//section//h2[text()='Детали ингредиента']")
    INGREDIENT = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")
    CROSS = (By.XPATH, "//button[contains(@class,'close')]")
    ORDER_GENERATOR = (By.XPATH, ".//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    COUNTER = (By.XPATH, "//ul[1]/a[1]//p[contains(@class, 'num')]")
    BUTTON_CREATE_ORDER = (By.XPATH, ".//main//button[text()='Оформить заказ']")
    LABEL_ORDER = (By.XPATH, ".//section//div/p[text()='Ваш заказ начали готовить']")