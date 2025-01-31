import logging
from app_pages.base_page import BasePage
from locators.ANDROID_LOCATORS.android_login_locators import AndroidLoginScreenLocators
from locators.ANDROID_LOCATORS.android_dashboard_locators import AndroidDashboardScreenLocators
from locators.IOS_LOCATORS.ios_login_locators import IOSLoginScreenLocators


class LoginPage(BasePage):
    """ Page Object Model for Login Page """

    def __init__(self, driver, platform):
        super().__init__(driver, platform)
        self.locators = (
            AndroidLoginScreenLocators if platform.lower() == "android" else IOSLoginScreenLocators
        )
        self.locator = AndroidDashboardScreenLocators if platform.lower() == "android" else IOSLoginScreenLocators

    def wait_for_login_screen(self):
        """ Wait until the login screen is displayed. """
        try:
            logging.info("🔄 Waiting for login screen to load...")
            self.wait_for_element(self.locators.LOGIN_BUTTON)
            logging.info("✅ Login screen is displayed.")
        except Exception as e:
            logging.error(f"❌ Login screen not displayed: {str(e)}")
            self.take_screenshot(name="login_screen_error")
            raise

    def enter_email(self, email):
        """ Enter email into the email field. """
        try:
            logging.info(f"🔐 Entering email: {email}")
            self.send_keys(self.locators.EMAIL_FIELD, email)
        except Exception as e:
            logging.error(f"❌ Failed to enter email: {str(e)}")
            self.take_screenshot(name="email_entry_error")
            raise

    def enter_password(self, password):
        """ Enter password into the password field. """
        try:
            logging.info("🔑 Entering password...")
            self.send_keys(self.locators.PASSWORD_FIELD, password)
        except Exception as e:
            logging.error(f"❌ Failed to enter password: {str(e)}")
            self.take_screenshot(name="password_entry_error")
            raise

    def click_login_button(self):
        """ Click the login button. """
        try:
            logging.info("📲 Clicking login button...")
            self.click(self.locators.LOGIN_BUTTON)
            logging.info("✅ Login button clicked successfully.")
        except Exception as e:
            logging.error(f"❌ Failed to click login button: {str(e)}")
            self.take_screenshot(name="login_button_click_error")
            raise

    def login(self, email, password):
        """ Perform the login operation. """
        self.wait_for_login_screen()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def is_login_successful(self):
        """ Check if login was successful by verifying dashboard visibility. """
        try:
            self.wait_for_element(self.locator.TITLE)
            logging.info("✅ Login successful!")
            return True
        except Exception as e:
            logging.error(f"❌ Login failed: {str(e)}")
            self.take_screenshot(name="login_failure_error")
            return False
