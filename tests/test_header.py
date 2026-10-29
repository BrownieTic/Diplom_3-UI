import allure
import pytest

from locators.header_locators import Locators as header_locators
from urls import Urls as urls

@allure.feature("Проверка шапки сайта")
class TestHeader():
    @allure.story("Переход по кнопкам в шапке сайта")
    @allure.title("Переход по клику на «Конструктор» и переход по клику на «Лента заказов»")
    @pytest.mark.parametrize('button_locator, url', [
        (header_locators.button_header_constructor, urls.MAIN_PAGE_URL),
        (header_locators.button_order_feed, urls.url_feed)
    ])
    def test_header_navigation(self, init_login_page, button_locator, url):
        init_login_page.invisible_overlay()
        init_login_page.click_button(button_locator)
        init_login_page.wait_load_url(url)
        with allure.step("Проверить текущий URL"):
            assert init_login_page.current_url() == url
