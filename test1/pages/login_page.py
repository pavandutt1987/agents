import logging

from playwright.sync_api import Page, expect

from test1.utils.logger import logger


class LoginPage:
    @logger
    def __init__(self, page: Page) -> None:
        self.page = page
        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Log In", exact=True)

    @logger
    def open(self, url: str) -> None:
        self.page.goto(url)

    @logger
    def login(self, username: str, password: str) -> None:
        logging.getLogger(__name__).info("Filling the email field")
        self.email_input.fill(username)
        logging.getLogger(__name__).info("Filling the password field")
        self.password_input.type(password)
        logging.getLogger(__name__).info("Submitting the login form")
        self.login_button.click()

    @logger
    def expect_login_success(self) -> None:
        expect(self.email_input).to_be_hidden()