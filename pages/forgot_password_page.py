import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def is_open(self):
        self.wait_path('/forgot-password')
        return self.find_visible(ForgotPasswordPageLocators.TITLE).is_displayed()

    @allure.step('Запросить восстановление для почты {email}')
    def request_password_reset(self, email):
        self.fill(ForgotPasswordPageLocators.EMAIL_INPUT, email)
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)
        self.wait_path('/reset-password')
