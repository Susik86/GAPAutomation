from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, platform):
        self.driver = driver
        self.platform = platform.lower()

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def find_element(self, locator, timeout=10):
        """
        Find an element with a timeout.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Element with locator {locator} not found."
        )

    def assert_visible(self, locator, timeout=10):
        """
        Assert that an element is visible on the screen.
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Element with locator {locator} is not visible."
        )
        assert element.is_displayed(), f"Element with locator {locator} is not visible."

    def assert_text(self, locator, expected_text, timeout=10):
        """
        Assert that the text of an element matches the expected text.
        """
        element = self.find_element(locator, timeout)
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'."

    def scroll_to_bottom(self, max_scrolls=10, timeout=3):
        """
        Scroll the screen to the bottom multiple times (up to max_scrolls).
        Supports both Android and iOS platforms.

        :param max_scrolls: Maximum number of times to scroll to the bottom.
        :param timeout: Time to wait after each scroll to allow the page to load.
        """
        for scroll in range(max_scrolls):
            try:
                if self.platform == "android":
                    # Use Android UiScrollable to scroll to the bottom
                    self.driver.find_element(By.ANDROID_UIAUTOMATOR,
                        "new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1)"
                    )
                elif self.platform == "ios":
                    # Use iOS-specific scrolling with swipe gestures
                    window_size = self.driver.get_window_size()
                    start_x = window_size["width"] // 2
                    start_y = window_size["height"] * 3 // 4
                    end_y = window_size["height"] // 4
                    self.driver.swipe(start_x, start_y, start_x, end_y, 800)
                else:
                    raise NotImplementedError("Scrolling is only implemented for Android and iOS.")

                # Wait after each scroll to allow the content to load
                WebDriverWait(self.driver, timeout).until(
                    lambda d: True  # Add custom logic here if needed to detect loading
                )

            except Exception as e:
                print(f"Scroll {scroll + 1} failed. Error: {e}")
                break



