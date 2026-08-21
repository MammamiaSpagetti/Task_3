import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открыть конструктор бургеров')
    def open_main_page(self):
        return self.open('/')

    def is_open(self):
        self.wait_path('/')
        return self.find_visible(MainPageLocators.TITLE).is_displayed()

    @allure.step('Открыть детали первого ингредиента')
    def open_first_ingredient_details(self):
        self.click(MainPageLocators.FIRST_INGREDIENT)
        self.find_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    def ingredient_details_are_open(self):
        return (
            '/ingredient/' in self.driver.current_url
            and self.find_visible(MainPageLocators.INGREDIENT_MODAL_TITLE).is_displayed()
        )

    def first_ingredient_counter(self):
        return int(self.text(MainPageLocators.FIRST_INGREDIENT_COUNTER))

    @allure.step('Добавить первый ингредиент в конструктор')
    def add_first_ingredient(self):
        source = self.find_visible(MainPageLocators.FIRST_INGREDIENT)
        target = self.find_visible(MainPageLocators.CONSTRUCTOR_BASKET)
        initial_counter = self.first_ingredient_counter()

        actions = (
            lambda: ActionChains(self.driver).drag_and_drop(source, target).perform(),
            lambda: ActionChains(self.driver)
            .move_to_element(source)
            .click_and_hold(source)
            .pause(0.3)
            .move_to_element(target)
            .pause(0.5)
            .release(target)
            .perform(),
            lambda: self.driver.execute_script(
                """
                const source = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();
                source.dispatchEvent(new DragEvent('dragstart', {
                    bubbles: true,
                    dataTransfer
                }));
                target.dispatchEvent(new DragEvent('dragenter', {
                    bubbles: true,
                    dataTransfer
                }));
                target.dispatchEvent(new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer
                }));
                target.dispatchEvent(new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer
                }));
                source.dispatchEvent(new DragEvent('dragend', {
                    bubbles: true,
                    dataTransfer
                }));
                """,
                source,
                target,
            ),
        )
        if self.driver.name == 'firefox':
            actions = (actions[2], actions[0], actions[1])

        for action in actions:
            action()
            try:
                self.wait.until(
                    lambda _: self.first_ingredient_counter() > initial_counter
                )
                return
            except TimeoutException:
                continue

        raise TimeoutException('Счётчик ингредиента не увеличился после переноса')

    @allure.step('Оформить заказ')
    def place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

        def actual_order_number(driver):
            for modal in driver.find_elements(*BasePageLocators.MODAL_CONTAINERS):
                if not modal.is_displayed() or 'идентификатор заказа' not in modal.text:
                    continue
                number = modal.find_element(*MainPageLocators.ORDER_NUMBER).text
                if number.isdigit() and number != '9999':
                    return int(number)
            return False

        return self.wait.until(actual_order_number)
