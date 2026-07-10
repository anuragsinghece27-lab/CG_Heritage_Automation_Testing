"""
Shared pytest fixtures and hooks.

- `driver` fixture: gives every test a fresh, isolated browser session
  and guarantees teardown (quit) even if the test fails.
- `pytest_runtest_makereport` hook: automatically captures a screenshot
  the moment any test fails, and embeds it into the pytest-html report.
"""

import os
import datetime
import pytest
from utils.driver_factory import get_driver

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


@pytest.fixture
def driver():
    drv = get_driver(headless=False)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach a screenshot to the HTML report whenever a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver", None)
        if drv is not None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = item.name.replace("[", "_").replace("]", "_")
            filename = f"{safe_name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOT_DIR, filename)
            try:
                drv.save_screenshot(filepath)
                if hasattr(report, "extra"):
                    pass  # extras handled below if pytest-html plugin present
                extra = getattr(report, "extra", [])
                try:
                    import pytest_html
                    rel_path = os.path.relpath(filepath, os.path.dirname(__file__) + "/reports")
                    extra.append(pytest_html.extras.image(filepath))
                    report.extra = extra
                except Exception:
                    pass
                print(f"\n[SCREENSHOT CAPTURED] {filepath}")
            except Exception as e:
                print(f"\n[SCREENSHOT FAILED] Could not capture screenshot: {e}")
