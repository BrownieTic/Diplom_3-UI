from selenium.webdriver.common.by import By

class Locators:
#Главная страница
    # Кнопка «Войти в аккаунт» на главной
    button_input_main_page = [By.CSS_SELECTOR, '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg']
    # Кнопка Оформить заказ
    button_order = [By.XPATH, './/button[text()="Оформить заказ"]']
    # Раздел Булки
    button_section_buns = [By.XPATH, './/span[text()="Булки"]/parent::div']
    start_of_section_buns = [By.XPATH, './/h2[text()="Булки"]']
    window_bun_main_page = [By.XPATH, '//p[text()="Краторная булка N-200i"]/parent::a']
    name_bun = [By.XPATH, '//p[text()="Краторная булка N-200i"]']
    counter_bun = [By.XPATH,'//p[text()="Краторная булка N-200i"]/preceding-sibling::div[@class="counter_counter__ZNLkj counter_default__28sqi"]/p']
    # Раздел Соусы
    button_section_sauces = [By.XPATH, './/span[text()="Соусы"]/parent::div']
    start_of_section_sauces = [By.XPATH, './/h2[text()="Соусы"]']
    name_sauce = [By.XPATH, './/p[text()="Соус фирменный Space Sauce"]']
    counter_sauce = [By.XPATH,'//p[text()="Соус фирменный Space Sauce"]/preceding-sibling::div[@class="counter_counter__ZNLkj counter_default__28sqi"]/p']
    # Раздел Начинки
    button_section_fillings = [By.XPATH, './/span[text()="Начинки"]/parent::div']
    start_of_section_fillings = [By.XPATH, './/h2[text()="Начинки"]']
    name_filling = [By.XPATH, './/p[text()="Мясо бессмертных моллюсков Protostomia"]']
    counter_filling_main_page = [By.XPATH,'//p[text()="Мясо бессмертных моллюсков Protostomia"]/preceding-sibling::div[@class="counter_counter__ZNLkj counter_default__28sqi"]/p']
    # Детали ингредиента окно
    ingredient_details = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    button_close_ingredient_details = [By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK"]
    # Окно идентификатора заказа
    button_order_identifier_close = [By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]']
    order_loading_animation = [By.CSS_SELECTOR, '.Modal_modal__loading__3534A']
    order_number = [By.XPATH, '//p[contains(text(), "идентификатор заказа")]/preceding-sibling::h2']
    # Секция конструктора бургера
    section_burger_constructor = [By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]']