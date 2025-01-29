from selenium.webdriver.common.by import By
from app_pages.base_page import BasePage
from locators.ANDROID_LOCATORS.android_dashboard_locators import AndroidDashboardScreenLocators
from locators.IOS_LOCATORS.ios_dashboard_locators import IOSDashboardScreenLocators


class DashboardPage(BasePage):
    def __init__(self, driver, platform):
        super().__init__(driver, platform)
        self.locators = AndroidDashboardScreenLocators if platform == "android" else IOSDashboardScreenLocators

    def click_on_Genius_Meter_tab(self):
        """
        Click on the Genius Meter tab.
        """
        self.click((By.ID, self.locators.GENIUS_METER_TAB))

    def assert_title_visible(self):
        """
        Assert that the title is visible.
        """
        self.assert_visible((By.ID, self.locators.TITLE))

    def assert_title_text(self, expected_text):
        """
        Assert that the title text matches the expected text.
        """
        self.assert_text((By.ID, self.locators.TITLE), expected_text)
