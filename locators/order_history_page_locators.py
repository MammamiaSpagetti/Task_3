from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDER_CARDS = (By.CSS_SELECTOR, "a[href^='/account/order-history/']")
