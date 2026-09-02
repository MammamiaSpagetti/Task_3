import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    def is_open(self):
        self.wait_path('/reset-password')
        return self.find_visible(ResetPasswordPageLocators.TITLE).is_displayed()

    @allure.step('Ввести новый пароль')
    def fill_password(self, password):
        self.fill(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Нажать кнопку показа пароля')
    def click_password_toggle(self):
        self.click(ResetPasswordPageLocators.PASSWORD_TOGGLE)

    def password_is_visible_and_active(self):
        password_input = self.find_visible(ResetPasswordPageLocators.PASSWORD_INPUT)
        parent_class = password_input.find_element('xpath', '..').get_attribute('class')
        return (
            password_input.get_attribute('type') == 'text'
            and 'input_status_active' in parent_class
            and self.driver.switch_to.active_element == password_input
        )
