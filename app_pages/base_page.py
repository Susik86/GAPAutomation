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
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Element with locator {locator} not found."
        )

    def assert_visible(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Element with locator {locator} is not visible."
        )
        assert element.is_displayed(), f"Element with locator {locator} is not visible."

    def assert_opened(self, locator, timeout=10):
        """Asserts that the page or component is opened by checking the visibility of a specific element."""
        self.assert_visible(locator, timeout)

    def assert_text(self, locator, expected_text, timeout=10):
        """Asserts that an element contains the expected text."""
        element = self.find_element(locator, timeout)
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'."

    def assert_enabled(self, locator, timeout=10):

        element = self.find_element(locator, timeout)
        assert element.is_enabled(), f"Element with locator {locator} is not enabled."

    def assert_attribute(self, locator, attribute_name, expected_value, timeout=10):
        """Asserts that an element has a specific attribute value."""
        element = self.find_element(locator, timeout)
        actual_value = element.get_attribute(attribute_name)
        assert actual_value == expected_value, (
            f"Expected attribute '{attribute_name}' to be '{expected_value}', but got '{actual_value}'."
        )

