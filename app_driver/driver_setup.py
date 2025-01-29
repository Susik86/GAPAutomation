from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from config_file.config import CONFIG

class DriverFactory:
    @staticmethod
    def create_driver(platform: str):
        if platform not in CONFIG:
            raise ValueError(f"Invalid platform: {platform}")

        capabilities = CONFIG[platform]

        options = AppiumOptions()
        for key, value in capabilities.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            options=options  # Use options instead of desired_capabilities
        )
        return driver
