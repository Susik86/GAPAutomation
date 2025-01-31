from selenium.webdriver.common.by import By

class AndroidLoginScreenLocators:

    EMAIL_FIELD = (By.ID, "com.gapinternational.genius.qa:id/emailEditText")
    PASSWORD_FIELD = (By.ID, "com.gapinternational.genius.qa:id/passwordEditText")
    LOGIN_BUTTON = (By.ID, "com.gapinternational.genius.qa:id/signInButton")

