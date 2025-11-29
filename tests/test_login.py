import pytest
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage

BASE_URL = "https://opensource-demo.orangehrmlive.com/"

@pytest.mark.regression
def test_admin_login_valid(driver, admin_creds):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    login.login(*admin_creds)
    assert "dashboard" in driver.current_url.lower()

@pytest.mark.regression
def test_admin_login_invalid_password(driver, admin_creds):
    driver.get(BASE_URL)
    login = LoginPage(driver)
    bad_pass = admin_creds[1] + "X"
    login.login(admin_creds[0], bad_pass)
    assert "Invalid credentials" in login.get_error_message()

@pytest.mark.regression
def test_logout_redirects_to_login(logged_in_admin):
    driver = logged_in_admin
    dash = DashboardPage(driver)
    dash.logout()
    assert "login" in driver.current_url.lower()
