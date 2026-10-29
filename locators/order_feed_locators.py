from selenium.webdriver.common.by import By

class Locators:
    # Лента заказов (правая часть страницы)
    counter_order_all_time = [By.XPATH, './/p[text() = "Выполнено за все время:"]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    counter_order_today = [By.XPATH, './/p[text() = "Выполнено за сегодня:"]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']
    section_in_progress = [By.XPATH, '//p[normalize-space()="В работе:"]/following-sibling::ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li']