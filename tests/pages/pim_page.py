from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    """Page object for PIM -> Add Employee."""

    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_EMP_BTN = (By.XPATH, "//a[contains(@href,'pim/addEmployee')]")

    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMP_ID = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div//input")
    CREATE_LOGIN_TOGGLE = (By.XPATH, "//p[text()='Create Login Details']/..//span")
    USERNAME = (By.XPATH, "//label[text()='Username']/../following-sibling::div//input")
    PASSWORD = (By.XPATH, "//label[text()='Password']/../following-sibling::div//input")
    CONFIRM_PASSWORD = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div//input")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")

    PERSONAL_DETAILS_HEADER = (By.XPATH, "//h6[contains(text(),'Personal Details')]")
    EMPLOYEE_FULLNAME_HEADER = (By.XPATH, "//h6[contains(@class,'oxd-text') and contains(@class,'--h6')]")

    def __init__(self, driver):
        self.driver = driver

    def open_add_employee(self) -> None:
        self.driver.find_element(*self.PIM_MENU).click()
        self.driver.find_element(*self.ADD_EMP_BTN).click()

    def create_employee_with_login(self, first_name, last_name, emp_id, username, password) -> None:
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

        emp_id_input = self.driver.find_element(*self.EMP_ID)
        emp_id_input.clear()
        emp_id_input.send_keys(emp_id)

        self.driver.find_element(*self.CREATE_LOGIN_TOGGLE).click()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(password)
        self.driver.find_element(*self.SAVE_BTN).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PERSONAL_DETAILS_HEADER)
        )

    def get_displayed_name(self) -> str:
        return self.driver.find_element(*self.EMPLOYEE_FULLNAME_HEADER).text
