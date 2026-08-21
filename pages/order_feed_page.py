import allure
from selenium.common.exceptions import TimeoutException

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Открыть ленту заказов')
    def open_order_feed(self):
        return self.open('/feed')

    def is_open(self):
        self.wait_path('/feed')
        return self.find_visible(OrderFeedPageLocators.TITLE).is_displayed()

    @allure.step('Открыть первый заказ в ленте')
    def open_first_order(self):
        self.click(OrderFeedPageLocators.ORDER_CARDS)
        self.visible_modal()

    def order_details_are_open(self):
        modal_text = self.visible_modal().text
        return (
            '/feed/' in self.driver.current_url
            and ('Cостав' in modal_text or 'Состав' in modal_text)
        )

    def total_counter(self):
        return int(self.text(OrderFeedPageLocators.TOTAL_COUNTER))

    def today_counter(self):
        return int(self.text(OrderFeedPageLocators.TODAY_COUNTER))

    def wait_total_counter_greater_than(self, initial_value):
        return self.wait.until(lambda _: self.total_counter() > initial_value)

    def wait_today_counter_greater_than(self, initial_value):
        return self.wait.until(lambda _: self.today_counter() > initial_value)

    def has_order_number(self, order_number):
        expected = f'#{int(order_number):06d}'
        try:
            return self.wait.until(
                lambda driver: any(
                    expected in card.text
                    for card in driver.find_elements(*OrderFeedPageLocators.ORDER_CARDS)
                )
            )
        except TimeoutException:
            return False

    def order_is_in_progress(self, order_number):
        expected = f'{int(order_number):06d}'
        try:
            return self.wait.until(
                lambda _: expected
                in self.text(OrderFeedPageLocators.IN_PROGRESS_LIST)
            )
        except TimeoutException:
            return False
