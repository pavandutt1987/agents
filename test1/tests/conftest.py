import logging
from collections.abc import Iterator

import pytest
from playwright.sync_api import Browser, Page, sync_playwright


test_logger = logging.getLogger(__name__)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--username", action="store", default=None, help="Login username")
    parser.addoption("--password", action="store", default=None, help="Login password")
    parser.addoption(
        "--browser",
        action="store",
        choices=("chromium", "firefox", "webkit"),
        default="chromium",
        help="Browser engine to use",
    )


@pytest.fixture(scope="session")
def browser(pytestconfig: pytest.Config) -> Iterator[Browser]:
    browser_name = pytestconfig.getoption("--browser")
    test_logger.info("Starting Playwright")
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, browser_name)
        test_logger.info("Launching %s browser", browser_name)
        browser = browser_type.launch(headless = False)
        test_logger.info("%s browser launched", browser_name)
        try:
            yield browser
        finally:
            test_logger.info("Closing %s browser", browser_name)
            browser.close()
            test_logger.info("Browser closed")


@pytest.fixture
def page(browser: Browser) -> Iterator[Page]:
    test_logger.info("Creating browser context")
    context = browser.new_context()
    try:
        test_logger.info("Creating browser page")
        page = context.new_page()
        test_logger.info("Browser page created")
        yield page
    finally:
        test_logger.info("Closing browser context")
        context.close()
        test_logger.info("Browser context closed")