from urllib.parse import urlparse

import allure
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from data import UI_TIMEOUT
from locators.base_page_locators import BasePageLocators
from urls import BASE_URL


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, UI_TIMEOUT)

    @allure.step('Открыть страницу {path}')
    def open(self, path):
        self.driver.get(f'{BASE_URL}{path}')
        return self

    def find_visible(self, locator):
        def visible_element(driver):
            for element in driver.find_elements(*locator):
                if element.is_displayed():
                    return element
            return False

        return self.wait.until(visible_element)

    def click(self, locator):
        element = self.find_visible(locator)
        self.wait.until(lambda _: element.is_enabled())
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click()', element)

    def fill(self, locator, value):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)

    def text(self, locator):
        return self.find_visible(locator).text

    def wait_path(self, expected_path):
        return self.wait.until(
            lambda driver: urlparse(driver.current_url).path == expected_path
        )

    def is_current_path(self, expected_path):
        return urlparse(self.driver.current_url).path == expected_path

    @allure.step('Перейти в конструктор')
    def click_constructor(self):
        self.click(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step('Перейти в ленту заказов')
    def click_order_feed(self):
        self.click(BasePageLocators.ORDER_FEED_LINK)

    @allure.step('Перейти в личный кабинет')
    def click_personal_account(self):
        self.click(BasePageLocators.PERSONAL_ACCOUNT_LINK)

    def visible_modal(self):
        return self.find_visible(BasePageLocators.MODAL_CONTAINERS)

    def is_modal_visible(self):
        try:
            self.visible_modal()
            return True
        except TimeoutException:
            return False

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click(BasePageLocators.MODAL_CLOSE_BUTTONS)
        self.wait.until(
            lambda driver: not any(
                element.is_displayed()
                for element in driver.find_elements(
                    *BasePageLocators.MODAL_CONTAINERS
                )
            )
        )
