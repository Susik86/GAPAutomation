from selenium.webdriver.common.by import By
from app_pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.ANDROID_LOCATORS.android_dashboard_locators import AndroidDashboardScreenLocators
from locators.IOS_LOCATORS.ios_dashboard_locators import IOSDashboardScreenLocators

from selenium.webdriver.common.by import By


class DashboardPage(BasePage):

    def __init__(self, driver, platform):
        super().__init__(driver, platform)
        self.driver = driver
        self.locators = AndroidDashboardScreenLocators if platform.lower() == "android" else IOSDashboardScreenLocators

    # def get_title_text(self):
    #     title_text = self.get_text(By.ID, self.locators.TITLE)
    #     return title_text

    def assert_title_visible(self):
        self.assert_visible((By.ID, self.locators.TITLE))

    def assert_title_text(self, expected_text):
        self.assert_text((By.ID, self.locators.TITLE), expected_text)







