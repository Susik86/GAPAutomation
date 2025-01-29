from selenium.webdriver.common.by import By
from app_pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.ANDROID_LOCATORS.android_login_locators import AndroidLoginScreenLocators
from locators.IOS_LOCATORS.ios_login_locators import IOSLoginScreenLocators


class LoginPage(BasePage):
    def __init__(self, driver, platform):
        super().__init__(driver, platform)
        self.locators = AndroidLoginScreenLocators if platform.lower() == "android" else IOSLoginScreenLocators

    def wait_for_login_screen(self):
        """
        Wait until the login screen is displayed.
        """
        self.assert_visible((By.ID, self.locators.EMAIL_FIELD))

    def login(self, email, password):
        """
        Perform the login operation.
        """
        self.wait_for_login_screen()

        # Enter email
        self.send_keys((By.ID, self.locators.EMAIL_FIELD), email)

        # Enter password
        self.send_keys((By.ID, self.locators.PASSWORD_FIELD), password)

        # Click login button
        self.click((By.ID, self.locators.LOGIN_BUTTON))
