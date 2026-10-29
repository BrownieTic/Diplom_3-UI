from page.base_page import BasePage
from locators.login_locators import Locators as login_locator

import allure

class LoginPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.find_element_on_page(login_locator.login_for_input_page).send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.find_element_on_page(login_locator.password_for_input_page).send_keys(password)

    @allure.step("Кликнуть по кнопке 'Войти'")
    def click_login_button(self):
        self.click_button(login_locator.button_input_page_input_path)

    @allure.step("Выполнить авторизацию")
    def login(self, email, password):
        self.invisible_overlay()
        self.wait_visibility_of_element(login_locator.login_for_input_page)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Ожидание сокрытия оверлея")
    def invisible_overlay(self):
        self.invisible_element(login_locator.overlay)
        