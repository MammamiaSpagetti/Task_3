from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    TITLE = (By.XPATH, "//h2[normalize-space()='Восстановление пароля']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    PASSWORD_TOGGLE = (
        By.CSS_SELECTOR,
        "input[name='Введите новый пароль'] + div.input__icon",
    )
