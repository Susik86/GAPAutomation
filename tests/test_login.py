import pytest
import logging
import random
from app_pages.login_page import LoginPage
from app_pages.dashboard_page import DashboardPage
from app_data.static_data.users import UsersData
from app_data.static_data.strings_en import StringsEn
from app_data.dynamic_data.data_handler import save_data, get_data

@pytest.mark.usefixtures("driver", "platform")  # ✅ FIX: Այստեղ ավելացվում է platform-ը
class TestLogin:
    """ Test Class for login functionality """

    def setup_method(self, method, driver, platform):  # ✅ FIX: Ստանում ենք driver-ը ֆիքստուրայից
        logging.info("🔹 Setting up Login Test")
        self.driver = driver
        self.platform = platform
        self.login_page = LoginPage(self.driver, self.platform)
        self.dashboard_page = DashboardPage(self.driver, self.platform)


    def test_login(self):
        """ Perform login with valid credentials and verify the dashboard title. """
        logging.info(f"🔹 Running login test on: {self.platform}")

        # Get user credentials dynamically
        email = random.choice(UsersData.valid_emails)
        password = UsersData.valid_password

        # Save login credentials
        save_data("last_used_email", email)
        save_data("last_used_password", password)

        logging.info(f"🔐 Logging in with: {email} / {password}")

        # Perform login
        self.login_page.login(email, password)

        # Ensure login is successful
        assert self.login_page.is_login_successful(), "❌ Login failed!"

        # Verify dashboard title visibility and text
        self.dashboard_page.assert_title_visible()
        self.dashboard_page.assert_title_text(StringsEn().DashboardPage().title)

        logging.info(f"✅ Dashboard title verified successfully: {StringsEn().DashboardPage().title}")
