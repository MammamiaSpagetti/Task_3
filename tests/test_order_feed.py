import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage


@allure.feature('Лента заказов')
class TestOrderFeed:
    @allure.title('Клик по заказу открывает окно с деталями')
    def test_click_order_opens_details_modal(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_order_feed()
        feed_page.open_first_order()

        assert feed_page.order_details_are_open()

    @allure.title('Заказ пользователя отображается в истории и общей ленте')
    def test_user_order_is_displayed_in_history_and_feed(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        main_page.open_main_page()
        main_page.add_first_ingredient()
        order_number = main_page.place_order()
        main_page.close_modal()
        main_page.click_personal_account()
        ProfilePage(authenticated_driver).click_order_history()
        history_page = OrderHistoryPage(authenticated_driver)
        order_is_in_history = history_page.has_order_number(order_number)
        history_page.click_order_feed()
        feed_page = OrderFeedPage(authenticated_driver)

        assert order_is_in_history
        assert feed_page.has_order_number(order_number)

    @allure.title('Новый заказ увеличивает счётчик за всё время')
    def test_new_order_increases_total_counter(self, authenticated_driver):
        feed_page = OrderFeedPage(authenticated_driver)
        feed_page.open_order_feed()
        initial_total = feed_page.total_counter()
        feed_page.click_constructor()
        main_page = MainPage(authenticated_driver)
        main_page.add_first_ingredient()
        main_page.place_order()
        main_page.close_modal()
        main_page.click_order_feed()

        assert feed_page.wait_total_counter_greater_than(initial_total)

    @allure.title('Новый заказ увеличивает счётчик за сегодня')
    def test_new_order_increases_today_counter(self, authenticated_driver):
        feed_page = OrderFeedPage(authenticated_driver)
        feed_page.open_order_feed()
        initial_today = feed_page.today_counter()
        feed_page.click_constructor()
        main_page = MainPage(authenticated_driver)
        main_page.add_first_ingredient()
        main_page.place_order()
        main_page.close_modal()
        main_page.click_order_feed()

        assert feed_page.wait_today_counter_greater_than(initial_today)

    @allure.title('Номер нового заказа появляется в разделе «В работе»')
    def test_new_order_number_appears_in_progress(self, authenticated_driver):
        main_page = MainPage(authenticated_driver)
        main_page.open_main_page()
        main_page.add_first_ingredient()
        order_number = main_page.place_order()
        main_page.close_modal()
        main_page.click_order_feed()

        assert OrderFeedPage(authenticated_driver).order_is_in_progress(
            order_number
        )
