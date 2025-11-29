from selenium.webdriver.common.by import By

class DashboardPage:
    """Page object for common dashboard/header elements."""

    USER_DROPDOWN = (By.CSS_SELECTOR, "p.oxd-userdropdown-name")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")
    PROFILE_NAME = (By.CSS_SELECTOR, "p.oxd-userdropdown-name")

    def __init__(self, driver):
        self.driver = driver

    def logout(self) -> None:
        self.driver.find_element(*self.USER_DROPDOWN).click()
        self.driver.find_element(*self.LOGOUT_LINK).click()

    def get_profile_name(self) -> str:
        return self.driver.find_element(*self.PROFILE_NAME).text
