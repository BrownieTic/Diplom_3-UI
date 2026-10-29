from page.base_page import BasePage
from urls import Urls as url
from locators.main_locators import Locators as main_locators

import allure

class MainPage(BasePage):
        @allure.step("Выбрать секцию, если еще не выбрана")
        def click_on_section(self, locator):
            element = self.find_element_on_page(locator)
            if "tab_type_current" in element.get_attribute("class"):
                return
            element.click()             
        
        @allure.step("Ожидать загрузки главной страницы")
        def wait_load_main_url(self):
            self.wait_load_url(url.MAIN_PAGE_URL)

        @allure.step("Открыть окно деталей ингредиента")
        def open_window_ingredient_details(self, locator=main_locators.window_bun_main_page):
            self.invisible_overlay()
            self.wait_to_be_clickable(locator)
            self.click_button(locator)

        @allure.step("Получить текст окна деталей ингредиента 'Детали ингредиента'")
        def get_text_ingredient_details(self):
            self.wait_visibility_of_element(main_locators.ingredient_details)
            text = self.get_text(main_locators.ingredient_details)
            return text

        @allure.step("Закрыть окно деталей ингредиента")
        def close_window_ingredient_details(self):
            self.wait_visibility_of_element(main_locators.button_close_ingredient_details)
            self.click_button(main_locators.button_close_ingredient_details)
            return self.is_window_closed(main_locators.button_close_ingredient_details)

        @allure.step("Получить название ингридиента из секции")
        def get_name_igredient(self, locator = main_locators.name_bun):
            return self.get_text(locator)

        @allure.step("Кликнуть по кнопке 'Оформить заказ'")
        def click_button_order(self):
            self.click_button(main_locators.button_order)

        @allure.step("Получить номер заказа")
        def get_order_number(self, locator=main_locators.order_number):
            order_number = self.get_text(locator)
            return order_number

        @allure.step("Ожидание полной загрузки страницы")
        def invisible_overlay(self):
            self.invisible_element(main_locators.order_loading_animation)

        @allure.step("Закрыть окно с номером заказа")
        def close_window_order_identifier(self):
            self.invisible_overlay()
            self.click_button(main_locators.button_order_identifier_close)

        @allure.step("Перетаскивает элемента")
        def drag_and_drop(self, source_locator = main_locators.name_bun, target_locator = main_locators.section_burger_constructor):
                """
                Перетаскивает элемент из source_locator в target_locator с использованием JavaScript.
                :param source_locator: Локатор элемента, который нужно перетащить.
                :param target_locator: Локатор элемента, куда нужно перетащить.
                """
                element_from = self.wait_visibility_of_element(source_locator)
                element_to = self.wait_visibility_of_element(target_locator)

                self.work_java(element_from, element_to)
      
        @allure.step("Выполнение шагов оформления заказа")
        def place_order(self):
            self.invisible_overlay()
            self.drag_and_drop()
            self.click_button_order()
            self.wait_visibility_of_element(main_locators.order_number)
            self.invisible_overlay()
            order_number = self.get_order_number()
            self.close_window_order_identifier()
            return order_number
