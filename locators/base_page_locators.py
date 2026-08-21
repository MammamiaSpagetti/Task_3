from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//header//a[.//p[normalize-space()='Конструктор']]",
    )
    ORDER_FEED_LINK = (By.CSS_SELECTOR, "header a[href='/feed']")
    PERSONAL_ACCOUNT_LINK = (By.CSS_SELECTOR, "header a[href='/account']")
    MODAL_CONTAINERS = (By.CSS_SELECTOR, "[class*='Modal_modal__container']")
    MODAL_CLOSE_BUTTONS = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
