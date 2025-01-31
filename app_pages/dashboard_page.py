import logging
from app_pages.base_page import BasePage
from locators.ANDROID_LOCATORS.android_dashboard_locators import AndroidDashboardScreenLocators
from locators.IOS_LOCATORS.ios_dashboard_locators import IOSDashboardScreenLocators


class DashboardPage(BasePage):
    def __init__(self, driver, platform):
        super().__init__(driver, platform)
        self.locators = AndroidDashboardScreenLocators if platform.lower() == "android" else IOSDashboardScreenLocators

    def click_on_Genius_Meter_tab(self):
        """Click on the Genius Meter tab."""
        try:
            logging.info("Clicking on Genius Meter tab...")
            self.wait_for_element_clickable(self.locators.GENIUS_METER_TAB)
            self.click(self.locators.GENIUS_METER_TAB)
            logging.info("Clicked on Genius Meter tab successfully.")
        except Exception as e:
            logging.error(f"Failed to click on Genius Meter tab: {str(e)}")
            self.take_screenshot(name="click_Genius_Meter_tab_error")
            raise

    def assert_title_visible(self):
        """Assert that the title is visible."""
        try:
            logging.info("Checking if title is visible...")
            self.wait_for_element(self.locators.TITLE)
            logging.info("Title is visible.")
        except Exception as e:
            logging.error(f"Title is not visible: {str(e)}")
            self.take_screenshot(name="title_visibility_error")
            raise

    def assert_title_text(self, expected_text):
        """Assert that the title text matches the expected text."""
        try:
            logging.info(f"Checking if title text matches '{expected_text}'...")
            actual_text = self.wait_for_element(self.locators.TITLE).text
            assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
            logging.info("Title text assertion passed.")
        except Exception as e:
            logging.error(f"Title text assertion failed: {str(e)}")
            self.take_screenshot(name="title_text_assertion_error")
            raise
