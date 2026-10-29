import pytest
from selenium import webdriver
from urls import Urls as url

from page.main_page import MainPage
from page.login_page import LoginPage
from page.header_page import HeaderPage
from page.order_feed_page import OrderFeedPage
from data import UserData as user_data

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    if "chrome" in request.param:
        driver = webdriver.Chrome()
    elif "firefox" in request.param:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_main_page(driver):
    driver.get(url.MAIN_PAGE_URL)
    return driver

@pytest.fixture(scope="function")
def driver_login_page(driver):
    driver.get(url.url_login)
    return driver

@pytest.fixture(scope="function")
def init_main_page(driver_main_page):
    page = MainPage(driver_main_page)
    return page

@pytest.fixture(scope="function")
def init_login_page(driver_login_page):
    page = LoginPage(driver_login_page)
    return page

@pytest.fixture(scope="function")
def driver_with_registered_user(init_login_page):
    init_login_page.login(user_data.USER_EMAIL, user_data.USER_PASSWORD)
    return init_login_page.driver

@pytest.fixture(scope="function")
def all_pages(driver_with_registered_user):
    header_page = HeaderPage(driver_with_registered_user)
    main_page = MainPage(driver_with_registered_user)
    order_feed_page = OrderFeedPage(driver_with_registered_user)
    return header_page, main_page, order_feed_page