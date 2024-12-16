import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from app_driver.driver_setup import Driver
from app_pages.login_page import LoginPage
from app_pages.dashboard_page import DashboardPage
from app_data.static_data.users import UsersData
from app_data.static_data.strings_en import StringsEn

@pytest.fixture(scope="module")
def driver(request):
    platform = request.config.getoption("--platform")
    driver_instance = Driver.create_driver(platform)
    yield driver_instance
    driver_instance.quit()

@pytest.mark.usefixtures("driver")
def test_open_app(driver):
    try:
        WebDriverWait(driver, 10)
    except Exception as e:
        raise AssertionError(f"App did not open to the login screen. Error: {e}")

@pytest.mark.usefixtures("driver")
def test_login(driver, request):

    platform = request.config.getoption("--platform")
    print(f"Platform received in test: {platform}")

    login_page = LoginPage(driver, platform)
    dashboard_page = DashboardPage(driver, platform)
    strings = StringsEn().DashboardPage()

    email = random.choice(UsersData.valid_emails)
    password = UsersData.valid_password
    login_page.login(email, password)
    dashboard_page.assert_title_visible()
    dashboard_page.assert_title_text(strings.title)
    print("cccc", strings.title)

