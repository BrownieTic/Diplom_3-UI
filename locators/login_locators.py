from selenium.webdriver.common.by import By

class Locators:
#Страница входа
    # Кнопка «Войти»
    button_input_page_input_path = [By.XPATH, './/button[text()="Войти"]']
    # Поля для входа
    login_for_input_page = [By.NAME, 'name']
    password_for_input_page = [By.NAME, 'Пароль']
    overlay = [By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr"]

    button_exit = [By.XPATH, './/button[text()="Войти"]']
