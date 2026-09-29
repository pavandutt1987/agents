import logging

import pytest
from playwright.sync_api import Page

from test1.pages.login_page import LoginPage
from test1.utils.logger import logger
from test1.utils.settings import LoginSettings


@logger
def test_user_can_log_in(page: Page, request: pytest.FixtureRequest) -> None:
    logging.getLogger(__name__).info("Loading login test settings")
    settings = LoginSettings.from_sources(
        username=request.config.getoption("--username"),
        password=request.config.getoption("--password"),
    )
    logging.getLogger(__name__).info("Creating login page object")
    login_page = LoginPage(page)

    login_page.open(settings.login_url)
    login_page.login(settings.username, settings.password)
    login_page.expect_login_success()