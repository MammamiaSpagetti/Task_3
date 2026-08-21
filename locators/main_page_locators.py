from selenium.webdriver.common.by import By


class MainPageLocators:
    TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")
    FIRST_INGREDIENT = (By.CSS_SELECTOR, "a[href^='/ingredient/']")
    FIRST_INGREDIENT_COUNTER = (
        By.CSS_SELECTOR,
        "a[href^='/ingredient/'] [class*='counter_counter__num']",
    )
    CONSTRUCTOR_BASKET = (
        By.CSS_SELECTOR,
        "section[class*='BurgerConstructor_basket']",
    )
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal__container')]"
        "//*[normalize-space()='Детали ингредиента']",
    )
    ORDER_NUMBER = (By.CSS_SELECTOR, "[class*='Modal_modal__title_shadow']")
