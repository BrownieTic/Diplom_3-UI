from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент на странице")
    def find_element_on_page(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @allure.step("Кликнуть по кнопке")
    def click_button(self, locator):
        self.wait_to_be_clickable(locator)
        self.find_element_on_page(locator).click()

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        self.wait_visibility_of_element(locator)
        element = self.find_element_on_page(locator)
        return element.text

    @allure.step("Установить значение элемента")
    def set_value(self, locator, text):
        self.find_element_on_page(locator).send_keys(text)

    @allure.step("Ожидать кликабельности элемента")
    def wait_to_be_clickable(self, locator):         
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Ожидать видимости элемента")
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидать загрузки страницы")
    def wait_load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))

    @allure.step("Ожидать невидимости элемента")
    def invisible_element(self, locator):
        def all_elements_invisible(driver):
            for element in driver.find_elements(*locator):
                try:
                    if element.is_displayed():
                        return False
                except StaleElementReferenceException:
                    continue
            return True

        WebDriverWait(self.driver, 10).until(all_elements_invisible)

    @allure.step("Получить текущий URL страницы")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание появление нужного значения")
    def wait_text_in_element(self, text, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(
                    locator,
                    text))    

    @allure.step("Ожидание закрытия окна")
    def is_window_closed(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Перетаскивает элемент из source_locator в target_locator с использованием JavaScript")
    def work_java(self, element_from, element_to):
                    self.driver.execute_script("""
                    var source = arguments[0];
                    var target = arguments[1];

                    var evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    source.dispatchEvent(evt);

                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);

                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);

                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    target.dispatchEvent(evt);

                    evt = document.createEvent("DragEvent");
                    evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                    source.dispatchEvent(evt);
                """, element_from, element_to)