import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def is_open(self):
        self.wait_path('/account/profile')
        return self.find_visible(ProfilePageLocators.PROFILE_LINK).is_displayed()

    @allure.step('Перейти в историю заказов')
    def click_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.wait_path('/account/order-history')

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_path('/login')
