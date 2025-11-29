from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyInfoPage:
    """Page object for My Info -> Personal Details (gender, blood type)."""

    MYINFO_MENU = (By.XPATH, "//span[text()='My Info']")
    # These locators may need adjustment based on actual DOM:
    GENDER_MALE = (By.XPATH, "//label[text()='Male']/preceding-sibling::input | //label[text()='Male']/ancestor::div[@class='oxd-radio-wrapper']")
    GENDER_FEMALE = (By.XPATH, "//label[text()='Female']/preceding-sibling::input | //label[text()='Female']/ancestor::div[@class='oxd-radio-wrapper']")
    BLOOD_TYPE_DROPDOWN = (By.XPATH, "//label[text()='Blood Type']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    BLOOD_TYPE_OPTION_BPOS = (By.XPATH, "//div[@role='listbox']//span[text()='B+']")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST = (By.XPATH, "//p[contains(@class,'oxd-text--toast-title') or text()='Success']")

    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        self.driver.find_element(*self.MYINFO_MENU).click()

    def set_gender_and_blood_type(self, gender: str = "Male", blood_type: str = "B+") -> None:
        # Scroll down in case elements are below the fold
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        if gender.lower() == "male":
            self.driver.find_element(*self.GENDER_MALE).click()
        else:
            self.driver.find_element(*self.GENDER_FEMALE).click()

        self.driver.find_element(*self.BLOOD_TYPE_DROPDOWN).click()
        # Only B+ is wired up for now (assignment requirement)
        self.driver.find_element(*self.BLOOD_TYPE_OPTION_BPOS).click()
        self.driver.find_element(*self.SAVE_BTN).click()

    def wait_for_success(self, timeout: int = 10) -> None:
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.SUCCESS_TOAST)
        )
