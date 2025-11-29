import pytest
from utils.employee_store import get_last_employee
from tests.pages.directory_page import DirectoryPage

@pytest.mark.regression
def test_directory_search_existing_employee(logged_in_admin):
    driver = logged_in_admin
    emp = get_last_employee()
    full_name = f"{emp['firstName']} {emp['lastName']}"
    directory = DirectoryPage(driver)
    directory.search_employee(full_name)
    assert directory.has_results()

@pytest.mark.regression
def test_directory_search_invalid_name(logged_in_admin):
    driver = logged_in_admin
    directory = DirectoryPage(driver)
    directory.search_employee("Random Name Not Exist 123")
    assert directory.has_no_records()
