# OrangeHRM Python + Pytest Automation 

This project is a Selenium + Pytest automation framework for the
[OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/), based on your assignment:

1. Login as admin (credentials from CLI). 
2. Create a new employee from the PIM menu with login details.
3. Save employee details into a JSON array file.
4. Search the employee in the Directory and verify it appears.
5. Logout.
6. Login with the newly created employee.
7. Assert full name is displayed near the profile icon.
8. Go to My Info, set gender and blood type B+, and save.
9. Run everything as a regression suite and generate an Allure report.

> **Note:** Locators are implemented against the current OrangeHRM demo UI structure.  
> If any locator breaks later, adjust the XPaths/CSS in `tests/pages/`.

---

## Tech Stack

- Python 3.9+
- Selenium WebDriver
- Pytest
- Allure (via `allure-pytest`)
- webdriver-manager

---

## Setup

1. **Clone the repository** (after you upload this project to GitHub):

   ```bash
   git clone <your-repo-url>.git
   cd <your-repo-folder>
   ```

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # on Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Allure CLI** (if not already installed)

   Follow the official Allure docs for your OS, then ensure `allure` command works:

   ```bash
   allure --version
   ```

---

## How to Run the Regression Suite

Admin credentials **must** be provided from the command line to respect the
"Get data from CLI" requirement.

```bash
pytest -m regression \
  --admin-user=Admin \
  --admin-pass=admin123 \
  --alluredir=allure-results
```

- `--admin-user` – admin username (from assignment, default demo value is `Admin`).
- `--admin-pass` – admin password (demo value `admin123`).
- `--alluredir` – folder where raw Allure results will be written.

`employees.json` is created/updated in the `data/` folder.  
Each successful employee creation test appends a new JSON object to the array.

---

## Generating and Viewing Allure Report

After running the tests:

```bash
allure serve allure-results
```

This will start a local web server and open the Allure dashboard in your browser.

Or generate a static report:

```bash
allure generate allure-results -o allure-report --clean
```

Then open `allure-report/index.html` in your browser.

> **Assignment Tip:**  
> Take screenshots of the Allure overview page and add them to your README
> (e.g. in `docs/screenshots/`) and reference them with markdown:
>
> ```md
> ![Allure Overview](docs/screenshots/allure-overview.png)
> ```

---

## Video Recording

Record the test execution (using OBS, built-in screen recorder, etc.).
You can either:

- Commit the video file to the repo (if small enough), or
- Upload to Google Drive and paste the shareable link here in the README.

Example:

```md
Automation Run Video: https://drive.google.com/your-video-link
```

---

## Test Structure & Scenarios

Main folders:

- `tests/pages/` – Page Object Model classes (Login, Dashboard, PIM, Directory, My Info).
- `tests/` – Test modules using pytest.
- `utils/` – Helpers for data generation and JSON employee store.
- `data/` – `employees.json` with created employee data.

### Sample Scenarios Covered

At least one **positive** and one **negative/edge** case per major scenario:

1. **Admin Login**
   - Valid admin login.
   - Invalid password login.

2. **Create Employee in PIM**
   - Create employee with valid data and login details.
   - Attempt creation with missing last name (placeholder negative).

3. **JSON Storage**
   - Successful employee object saved to `employees.json` and appended.

4. **Directory Search**
   - Search existing employee by full name (found).
   - Search random name (no records found).

5. **Logout**
   - Logout redirects back to login page.

6. **Employee Login**
   - Login with newly created employee credentials.
   - Login with invalid password fails.

7. **Profile Name Check**
   - Employee full name appears beside profile icon.

8. **My Info – Gender & Blood Type**
   - Set gender and blood type B+ and save successfully.
   - Placeholder for validation negative (update after checking actual DOM).

All tests are marked with `@pytest.mark.regression` so running with `-m regression` executes the whole suite.

---

## .gitignore (Per Assignment)

The project `.gitignore` already excludes:

- `build/`, `target/`
- `.idea/`
- `.gradle/`, `gradle/`
- `allure-results/`, `allure-report/`, `allure-reports/`
- Python caches and virtual environments

You can modify it as needed, but keep the required folders ignored for submission.

---

## Notes

- Some locators use XPath and may require a tiny tweak if the OrangeHRM DOM changes.
- For your assignment, you can:
  - Adjust locators after inspecting the site.
  - Replace placeholder `assert True` in negative tests with real validation checks.
  - Capture Allure screenshots, video, and upload everything to GitHub as required.
