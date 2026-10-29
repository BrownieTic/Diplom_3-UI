from locators.header_locators import Locators
from urls import Urls as url
from page.base_page import BasePage
import allure

class HeaderPage(BasePage):

    @allure.step("Кликнуть по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.invisible_element(Locators.loading_overlay)
        self.click_button(Locators.button_header_constructor)
        self.wait_load_url(url.MAIN_PAGE_URL)

    @allure.step("Кликнуть по логотипу")
    def click_logo_button(self):
        self.click_button(Locators.button_header_logo)

    @allure.step("Кликнуть по кнопке 'Лента заказов'")
    def click_order_feed_button(self):
        self.invisible_element(Locators.loading_overlay)
        self.click_button(Locators.button_order_feed)
        self.wait_load_url(url.url_feed)
