import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature('Основной функционал')
class TestMainFunctionality:
    @allure.title('Переход из ленты заказов в конструктор')
    def test_click_constructor_opens_main_page(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed()
        feed_page.click_constructor()

        assert MainPage(driver).is_open()

    @allure.title('Переход из конструктора в ленту заказов')
    def test_click_order_feed_opens_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_feed()

        assert OrderFeedPage(driver).is_open()

    @allure.title('Клик по ингредиенту открывает окно деталей')
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_first_ingredient_details()

        assert main_page.ingredient_details_are_open()

    @allure.title('Крестик закрывает окно деталей ингредиента')
    def test_close_button_closes_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_first_ingredient_details()
        main_page.close_modal()

        assert not main_page.is_modal_visible()

    @allure.title('Добавление ингредиента увеличивает его счётчик')
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        initial_counter = main_page.first_ingredient_counter()
        main_page.add_first_ingredient()

        assert main_page.first_ingredient_counter() > initial_counter

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_place_order(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        main_page.open_main_page()
        main_page.add_first_ingredient()

        assert main_page.place_order() > 0
