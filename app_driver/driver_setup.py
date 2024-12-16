from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config

class Driver:
    @staticmethod
    def create_driver(platform: str):
        # Fetch capabilities from the Config class
        capabilities = Config.get_capabilities(platform)
        print(f"Capabilities received: {capabilities}")

        # Create AppiumOptions for Android
        if platform == "android":
            options = UiAutomator2Options()
            for key, value in capabilities.items():
                options.set_capability(key, value)
        else:
            raise ValueError(f"Unsupported platform: {platform}")

        # Start the driver
        try:
            driver = webdriver.Remote(
                command_executor="http://localhost:4723/wd/hub",
                options=options
            )
            print("App successfully launched.")
            return driver
        except Exception as e:
            print(f"Error launching the app: {e}")
            raise RuntimeError(f"Failed to create driver for platform {platform}: {e}")
