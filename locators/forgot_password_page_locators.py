from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    TITLE = (By.XPATH, "//h2[normalize-space()='Восстановление пароля']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "form input[type='text']")
    RESTORE_BUTTON = (By.XPATH, "//button[normalize-space()='Восстановить']")
