from selenium.webdriver.common.by import By

class Locators:
#Шапка
    # Конструктор
    button_header_constructor = [By.XPATH, './/p[text() = "Конструктор"]']
    # Логотип
    button_header_logo = [By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2']
    # Личный кабинет
    button_header_profile = [By.CSS_SELECTOR, 'a[href*="/account"]']
    # Лента заказов
    button_order_feed = [By.XPATH, './/p[text() = "Лента Заказов"]']
    # Оверлей
    loading_overlay = [By.CSS_SELECTOR, '.Modal_modal_overlay__x2ZCr']
