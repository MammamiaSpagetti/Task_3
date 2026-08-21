from selenium.common.exceptions import TimeoutException

from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    def is_open(self):
        return self.is_current_path('/account/order-history')

    def has_order_number(self, order_number):
        expected = f'#{int(order_number):06d}'
        try:
            return self.wait.until(
                lambda driver: any(
                    expected in card.text
                    for card in driver.find_elements(
                        *OrderHistoryPageLocators.ORDER_CARDS
                    )
                )
            )
        except TimeoutException:
            return False
