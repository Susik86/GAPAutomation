class Config:
    CONFIG = {
        "android": {
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:deviceName": "emulator-5556",
            "appium:app": "/Users/susannakarapetyan/Desktop/QA.apk",
            "appium:platformVersion": "10",
            "appium:appPackage": "com.gapinternational.genius.qa",
            "appium:appWaitActivity": "com.gapinternational.genius.presentation.screen.splash.StartActivity",
            "appium:autoGrantPermissions": True
        },
    }

    @staticmethod
    def get_capabilities(platform: str):
        if platform not in Config.CONFIG:
            raise ValueError(f"Invalid platform: {platform}")
        return Config.CONFIG[platform]
