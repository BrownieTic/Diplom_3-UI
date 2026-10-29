import allure
import pytest

from locators.order_feed_locators import Locators as order_feed_locators

@allure.feature("Проверка страницы «Лента заказов»")
class TestOrderFeed():
    @allure.story("Проверка счетчиков на странице «Лента заказов»")
    @allure.title("Все счетчики заказов увеличиваются при создании нового заказа")
    @pytest.mark.parametrize("counter", [
        order_feed_locators.counter_order_all_time,
        order_feed_locators.counter_order_today])
    def test_counter_all_time_increase_when_a_new_order_is_created(self, all_pages, counter):
        header_page, main_page, order_feed_page = all_pages
        header_page.click_order_feed_button()
        old_counter = order_feed_page.get_text(counter)
        header_page.click_constructor_button()
        main_page.place_order()
        header_page.click_order_feed_button()
        new_counter = order_feed_page.get_text(counter)
        with allure.step("Проверить успешное увеличение счетчика"):
            assert new_counter == str(int(old_counter) + 1)

    @allure.story("Проверка отображения заказов на странице «Лента заказов»")
    @allure.title("Номер нового заказа отображается в разделе «В работе»")
    def test_after_new_order_his_number_is_displayed_in_order_feed(self, all_pages):
        header_page, main_page, order_feed_page = all_pages
        order_number = main_page.place_order()
        header_page.click_order_feed_button()
        order_in_progress_section = order_feed_page.get_order_number_from_progress_section(order_number)
        with allure.step("Проверить успешное отображение номера заказа"):
            assert f"0{int(order_number)}" in order_in_progress_section