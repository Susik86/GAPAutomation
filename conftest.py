import pytest
import logging
from app_driver.driver_setup import DriverFactory

def pytest_addoption(parser):
    """ Adds custom command-line options for pytest """
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Platform to run tests on: android or ios",
    )

@pytest.fixture(scope="session")
def platform(request):
    """ Retrieves the platform from pytest command-line options """
    return request.config.getoption("--platform").lower()

@pytest.fixture(scope="session")
def driver(platform):
    """ Initializes the Appium driver before test session starts. """
    logging.info(f"🚀 Initializing Appium driver for platform: {platform}")
    driver = DriverFactory.create_driver(platform)
    yield driver
    logging.info("🔄 Quitting Appium driver...")
    driver.quit()
