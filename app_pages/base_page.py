import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform.lower()
        self.wait = WebDriverWait(driver, 10)  # Default Timeout

    def find_element(self, locator, timeout=10):
        """Find an element with a timeout."""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            logging.info(f"Found element: {locator}")
            return element
        except Exception as e:
            logging.error(f"Could not find element: {locator}. Error: {str(e)}")
            self.take_screenshot()
            raise

    def wait_for_element(self, locator, timeout=10):
        """Wait until an element is visible and return it."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            logging.error(f"Element not visible: {locator}. Error: {str(e)}")
            self.take_screenshot()
            raise

    def wait_for_element_clickable(self, locator, timeout=10):
        """Wait until an element is clickable and return it."""
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except Exception as e:
            logging.error(f"Element not clickable: {locator}. Error: {str(e)}")
            self.take_screenshot()
            raise

    def click(self, locator):
        """Click an element after waiting for it to be clickable."""
        try:
            element = self.wait_for_element_clickable(locator)
            element.click()
            logging.info(f"Clicked on element: {locator}")
        except Exception as e:
            logging.error(f"Failed to click on {locator}. Error: {str(e)}")
            self.take_screenshot()
            raise

    def send_keys(self, locator, text):
        """Send text to an input field after waiting for it to be visible."""
        try:
            element = self.wait_for_element(locator)
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered text '{text}' in {locator}")
        except Exception as e:
            logging.error(f"Failed to enter text in {locator}. Error: {str(e)}")
            self.take_screenshot()
            raise

    def take_screenshot(self, name="screenshot"):
        """Take a screenshot in case of failure."""
        screenshot_path = f"{name}.png"
        self.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved: {screenshot_path}")

    def scroll_to_bottom(self, max_scrolls=10, timeout=3):
        """Scroll the screen to the bottom multiple times (up to max_scrolls)."""
        for scroll in range(max_scrolls):
            try:
                if self.platform == "android":
                    self.driver.find_element(
                        By.ANDROID_UIAUTOMATOR,
                        "new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1)"
                    )
                elif self.platform == "ios":
                    window_size = self.driver.get_window_size()
                    start_x = window_size["width"] // 2
                    start_y = window_size["height"] * 3 // 4
                    end_y = window_size["height"] // 4
                    self.driver.swipe(start_x, start_y, start_x, end_y, 800)
                else:
                    raise NotImplementedError("Scrolling is only implemented for Android and iOS.")

                WebDriverWait(self.driver, timeout).until(lambda d: True)
                logging.info(f"Scrolled down ({scroll + 1}/{max_scrolls})")
            except Exception as e:
                logging.error(f"Scroll {scroll + 1} failed. Error: {str(e)}")
                self.take_screenshot()
                break
