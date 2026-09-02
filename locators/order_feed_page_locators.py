from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']")
    ORDER_CARDS = (By.CSS_SELECTOR, "a[href^='/feed/']")
    TOTAL_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за все время:']/following-sibling::p[1]",
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за сегодня:']/following-sibling::p[1]",
    )
    IN_PROGRESS_LIST = (
        By.CSS_SELECTOR,
        "ul[class*='OrderFeed_orderListReady']",
    )
