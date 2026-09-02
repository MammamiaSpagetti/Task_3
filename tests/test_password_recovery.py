import allure

from data import generate_email
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля')
    def test_click_forgot_password_opens_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_forgot_password()

        assert ForgotPasswordPage(driver).is_open()

    @allure.title('Ввод почты и переход к сбросу пароля')
    def test_submit_email_opens_reset_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_forgot_password()
        ForgotPasswordPage(driver).request_password_reset(generate_email())

        assert ResetPasswordPage(driver).is_open()

    @allure.title('Кнопка показа пароля активирует и подсвечивает поле')
    def test_password_toggle_activates_password_field(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.click_forgot_password()
        ForgotPasswordPage(driver).request_password_reset(generate_email())
        reset_page = ResetPasswordPage(driver)
        reset_page.fill_password('NewPassword123')
        reset_page.click_password_toggle()

        assert reset_page.password_is_visible_and_active()
