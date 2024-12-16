from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from app_pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.ANDROID_LOCATORS.android_login_locators import AndroidLoginScreenLocators
from locators.IOS_LOCATORS.ios_login_locators import IOSLoginScreenLocators

class LoginPage(BasePage):
    def __init__(self, driver, platform):
        super().__init__(driver, platform)  # Call the parent class constructor
        self.driver = driver
        self.locators = AndroidLoginScreenLocators if platform.lower() == "android" else IOSLoginScreenLocators

    def wait_for_login_screen(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, self.locators.EMAIL_FIELD)))

    def login(self, email, password):
        self.wait_for_login_screen()

        email_field = self.driver.find_element(By.ID, self.locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.ID, self.locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.ID, self.locators.LOGIN_BUTTON)
        login_button.click()
        WebDriverWait(self.driver, 10)







