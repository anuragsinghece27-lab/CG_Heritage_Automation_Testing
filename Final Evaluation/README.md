# SauceDemo Automation Suite
### Python + Selenium | Final Hands-On Evaluation

Automation project covering the 4 required business test cases for
`https://www.saucedemo.com`, `https://demoqa.com/buttons`, and
`https://the-internet.herokuapp.com/javascript_alerts`.

---

## 1. Project Structure

```
saucedemo_automation/
├── pages/                          # Page Object Model (one class per page)
│   ├── base_page.py                 # Shared explicit-wait helpers
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── buttons_page.py              # demoqa.com/buttons
│   └── js_alerts_page.py            # the-internet.herokuapp.com/javascript_alerts
│
├── tests/                          # Test cases (grouped exactly per the spec)
│   ├── test_1_login.py              # TC1 - User Authentication (10 marks)
│   ├── test_2_purchase_journey.py   # TC2 - Product Purchase Journey (15 marks)
│   ├── test_3_multiple_users.py     # TC3 - Multiple User Validation (10 marks)
│   └── test_4_browser_interactions.py # TC4 - Browser Interaction Validation (10 marks)
│
├── utils/
│   ├── config.py                    # URLs, credentials, test data, timeouts
│   └── driver_factory.py            # Centralised WebDriver creation
│
├── reports/                         # execution_report.html + login_results.csv generated here
├── screenshots/                     # Auto-captured on any test failure
├── conftest.py                      # `driver` fixture + screenshot-on-failure hook
├── pytest.ini                       # pytest config (markers, HTML report path)
├── requirements.txt
└── README.md
```

This follows the **Page Object Model (POM)**: locators and page interactions
live in `pages/`, test logic and assertions live in `tests/`, and reusable
config/data lives in `utils/`. This keeps tests readable and means a UI
change only requires updating one page object, not every test.

---

## 2. Prerequisites

- Python 3.9+
- Google Chrome installed (the suite uses `webdriver-manager`, which
  auto-downloads the matching ChromeDriver — no manual driver setup needed)
- Internet access to saucedemo.com, demoqa.com, and the-internet.herokuapp.com

> **Note:** This project was authored and syntax-validated in a sandboxed
> environment without outbound internet/browser access, so the suite could
> not be executed live from here. All files were compiled (`py_compile`)
> and all 14 tests collect successfully via `pytest --collect-only`
> (see below). Run the commands in Section 4 on your own machine to
> produce the live HTML report and any failure screenshots for submission.

---

## 3. Setup

```bash
# 1. Extract/clone the project, then move into it
cd saucedemo_automation

# 2. (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 4. Running the Suite

Run everything (all 4 test cases):
```bash
pytest
```

Run a single test case using its marker:
```bash
pytest -m tc1     # Test Case 1 - User Authentication
pytest -m tc2     # Test Case 2 - Product Purchase Journey
pytest -m tc3     # Test Case 3 - Multiple User Validation
pytest -m tc4     # Test Case 4 - Browser Interaction Validation
```

Run a specific file:
```bash
pytest tests/test_2_purchase_journey.py -v
```

Run headless (no visible browser window, e.g. for CI):
```python
# in conftest.py, change:
drv = get_driver(headless=False)
# to:
drv = get_driver(headless=True)
```

### Verifying the project without a browser (sanity check)
```bash
pytest --collect-only -q
```
This confirms every test file imports correctly and all 14 tests are
discovered, without needing a browser or network access.

---

## 5. Outputs / Evidence

After running `pytest`, you will find:

| Artifact | Location |
|---|---|
| HTML execution report (pass/fail, timings, embedded failure screenshots) | `reports/execution_report.html` |
| Data-driven login results (Test Case 3) | `reports/login_results.csv` |
| Screenshots of any failed test | `screenshots/` (also embedded in the HTML report) |
| Console/CLI log | printed to terminal during the run |

Open `reports/execution_report.html` in any browser to review the full run.

---

## 6. Test Case Coverage Summary

| Test Case | File | Marks | What it validates |
|---|---|---|---|
| TC1 – User Authentication | `test_1_login.py` | 10 | Login page load, valid login → Products page, logout, invalid login → error message |
| TC2 – Product Purchase Journey | `test_2_purchase_journey.py` | 15 | Login → sort ascending by price → add Sauce Labs Backpack → cart verification → checkout → customer details → order confirmation |
| TC3 – Multiple User Validation | `test_3_multiple_users.py` | 10 | Data-driven login across `standard_user`, `locked_out_user`, `problem_user`, and a wrong-password case; results recorded to CSV |
| TC4 – Browser Interaction Validation | `test_4_browser_interactions.py` | 10 | Double-click & right-click on demoqa.com; JS Alert, Confirm, and Prompt (accept + dismiss) on the-internet.herokuapp.com, with message verification |
| TC5 – Test Execution Evidence | (this README + `reports/` + `screenshots/`) | 5 | Source code, HTML report, screenshots, and organized project structure |

---

## 7. Design Notes

- **Explicit waits everywhere** (`WebDriverWait` in `base_page.py`) instead
  of `time.sleep()`, so the suite is resilient to normal page-load latency
  without being needlessly slow.
- **Data-driven testing** for Test Case 3 via `pytest.mark.parametrize`,
  fed from a single source of truth (`utils/config.py`), so adding a new
  user/password combination is a one-line change.
- **Automatic screenshot capture on failure** via a `pytest_runtest_makereport`
  hook in `conftest.py` — no need to remember to add screenshot code inside
  each test.
- **Ad-overlay handling** on demoqa.com (`ButtonsPage._dismiss_overlays`)
  since that site frequently injects ad banners that intercept clicks.
