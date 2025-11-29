from selenium.webdriver.common.by import By

class LoginPage:
    """Page object for the OrangeHRM login page."""

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MSG = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username: str, password: str) -> None:
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_error_message(self) -> str:
        return self.driver.find_element(*self.ERROR_MSG).text
