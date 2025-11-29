from selenium.webdriver.common.by import By

class DirectoryPage:
    """Page object for Directory search."""

    DIRECTORY_MENU = (By.XPATH, "//span[text()='Directory']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")
    SEARCH_BTN = (By.XPATH, "//button[@type='submit']")
    NO_RECORDS = (By.XPATH, "//span[text()='No Records Found']")
    TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div")

    def __init__(self, driver):
        self.driver = driver

    def search_employee(self, name: str) -> None:
        self.driver.find_element(*self.DIRECTORY_MENU).click()
        name_input = self.driver.find_element(*self.EMPLOYEE_NAME_INPUT)
        name_input.clear()
        name_input.send_keys(name)
        # NOTE: For this field there may be an autocomplete dropdown; if so
        # you might need to select the first suggestion here.
        self.driver.find_element(*self.SEARCH_BTN).click()

    def has_results(self) -> bool:
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows) > 0

    def has_no_records(self) -> bool:
        return len(self.driver.find_elements(*self.NO_RECORDS)) > 0
