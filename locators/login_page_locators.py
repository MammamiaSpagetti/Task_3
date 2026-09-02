from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "form input[type='text']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "form input[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/forgot-password']")
