import pytest
from utils.employee_store import get_last_employee
from tests.pages.login_page import LoginPage
from tests.pages.myinfo_page import MyInfoPage

BASE_URL = "https://opensource-demo.orangehrmlive.com/"

@pytest.mark.regression
def test_update_gender_and_blood_type(driver):
    emp = get_last_employee()
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(emp["username"], emp["password"])

    myinfo = MyInfoPage(driver)
    myinfo.open()
    myinfo.set_gender_and_blood_type(gender="Male", blood_type="B+")
    myinfo.wait_for_success()

@pytest.mark.regression
def test_blood_type_validation_placeholder(driver):
    """Placeholder negative test for My Info validation.

    Once you inspect the DOM, replace this with a real assertion, e.g.:
    - Try to save without selecting gender or blood type.
    - Assert that a validation message is shown.
    """
    emp = get_last_employee()
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(emp["username"], emp["password"])

    myinfo = MyInfoPage(driver)
    myinfo.open()
    # TODO: implement real negative scenario based on actual UI behaviour
    assert True
