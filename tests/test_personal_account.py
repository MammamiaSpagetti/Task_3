import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage


@allure.feature('Личный кабинет')
class TestPersonalAccount:
    @allure.title('Переход в личный кабинет')
    def test_click_personal_account_opens_profile(self, authenticated_driver):
        MainPage(authenticated_driver).click_personal_account()

        assert ProfilePage(authenticated_driver).is_open()

    @allure.title('Переход в историю заказов')
    def test_click_order_history_opens_order_history(self, authenticated_driver):
        MainPage(authenticated_driver).click_personal_account()
        ProfilePage(authenticated_driver).click_order_history()

        assert OrderHistoryPage(authenticated_driver).is_open()

    @allure.title('Выход из аккаунта')
    def test_logout_returns_to_login_page(self, authenticated_driver):
        MainPage(authenticated_driver).click_personal_account()
        ProfilePage(authenticated_driver).logout()

        assert LoginPage(authenticated_driver).is_open()
