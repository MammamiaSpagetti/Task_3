from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[normalize-space()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[normalize-space()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")
