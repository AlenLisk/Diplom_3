from selenium.webdriver.common.by import By
class ForgotPasswordPageLocators:
    FIELD_EMAIL = (By.NAME, 'name')
    BUTTON_RESTORE = (By.XPATH, ".//button[text()='Восстановить']")
    BUTTON_SHOW_PASSWORD = (By.XPATH, '//div[contains(@class,"icon-action")]')
    TITLE_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    INPUT_STATUS_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'

