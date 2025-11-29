import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://opensource-demo.orangehrmlive.com/"

def pytest_addoption(parser):
    parser.addoption("--admin-user", action="store", default=None,
                     help="Admin username for OrangeHRM")
    parser.addoption("--admin-pass", action="store", default=None,
                     help="Admin password for OrangeHRM")

@pytest.fixture(scope="session")
def admin_creds(request):
    user = request.config.getoption("--admin-user")
    pw = request.config.getoption("--admin-pass")
    if not user or not pw:
        raise RuntimeError("Please provide --admin-user and --admin-pass to pytest "
                           "using --admin-user and --admin-pass CLI options.")
    return user, pw

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Uncomment to run headless in CI
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_admin(driver, admin_creds):
    """Logs in as admin and returns the driver."""
    from tests.pages.login_page import LoginPage
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(admin_creds[0], admin_creds[1])
    return driver
