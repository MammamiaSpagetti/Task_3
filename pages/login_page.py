import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Открыть страницу входа')
    def open_login_page(self):
        return self.open('/login')

    @allure.step('Перейти к восстановлению пароля')
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Войти под пользователем {email}')
    def login(self, email, password):
        self.fill(LoginPageLocators.EMAIL_INPUT, email)
        self.fill(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_path('/')

    def is_open(self):
        return self.is_current_path('/login')
