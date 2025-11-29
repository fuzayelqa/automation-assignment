import pytest
from utils.employee_store import get_last_employee
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage

BASE_URL = "https://opensource-demo.orangehrmlive.com/"

@pytest.mark.regression
def test_employee_login_valid(driver):
    emp = get_last_employee()
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(emp["username"], emp["password"])
    assert "dashboard" in driver.current_url.lower()

@pytest.mark.regression
def test_employee_login_invalid_password(driver):
    emp = get_last_employee()
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(emp["username"], emp["password"] + "X")
    assert "Invalid credentials" in login.get_error_message()

@pytest.mark.regression
def test_employee_full_name_displayed(driver):
    emp = get_last_employee()
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(emp["username"], emp["password"])

    dash = DashboardPage(driver)
    full_name_ui = dash.get_profile_name()
    expected_name = f"{emp['firstName']} {emp['lastName']}"
    assert expected_name in full_name_ui
