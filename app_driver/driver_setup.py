import logging
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from config_file.config import CONFIG

class DriverFactory:
    @staticmethod
    def create_driver(platform: str):
        """ Create and return an Appium driver based on the platform. """

        if platform.lower() not in CONFIG:
            raise ValueError(f"Invalid platform: {platform}. Choose from {list(CONFIG.keys())}")

        logging.info(f"Starting Appium driver for platform: {platform}")

        capabilities = CONFIG[platform.lower()]  # Convert platform name to lowercase for consistency
        options = AppiumOptions()

        for key, value in capabilities.items():
            options.set_capability(key, value)

        try:
            driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4723/wd/hub',  # Local Appium Server
                options=options  # Using new AppiumOptions
            )
            driver.implicitly_wait(10)  # Default implicit wait for elements
            logging.info(f"Appium driver started successfully for {platform}")
            return driver
        except Exception as e:
            logging.error(f"Failed to start Appium driver for {platform}. Error: {str(e)}")
            raise
