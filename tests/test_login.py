import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app_pages.login_page import LoginPage
from app_pages.dashboard_page import DashboardPage
from app_data.static_data.users import UsersData
from app_data.static_data.strings_en import StringsEn
from app_driver.driver_setup import DriverFactory

from locators.ANDROID_LOCATORS.android_login_locators import AndroidLoginScreenLocators


@pytest.fixture
def driver(request):
    """
    Initializes the Appium driver based on the platform specified in command line arguments.
    """
    platform = request.config.getoption("--platform", default="android")
    driver = DriverFactory.create_driver(platform)
    yield driver
    driver.quit()


# Test to verify the app opens to the login screen
def test_open_app(driver, request):
    """
    Verify the login screen is displayed.
    """
    try:
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.ID, AndroidLoginScreenLocators.LOGIN_BUTTON)
        )
        print("Login screen is displayed.")
    except Exception as e:
        raise AssertionError(f"Login screen not found. Error: {e}")


# Test for login and dashboard title verification
def test_login(driver, request):
    """
    Perform login with valid credentials and verify the dashboard title.
    """
    # Fetch platform dynamically
    platform = request.config.getoption("--platform", default="android")
    print(f"Platform received in test: {platform}")

    # Initialize Pages
    login_page = LoginPage(driver, platform)
    dashboard_page = DashboardPage(driver, platform)
    strings = StringsEn().DashboardPage()

    # Get user credentials
    email = random.choice(UsersData.valid_emails)
    password = UsersData.valid_password

    # Perform login
    login_page.login(email, password)

    # Verify dashboard title visibility and text
    dashboard_page.assert_title_visible()
    dashboard_page.assert_title_text(strings.title)
    print(f"Dashboard title verified: {strings.title}")
