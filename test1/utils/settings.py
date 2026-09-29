import os
from dataclasses import dataclass

from test1.utils.logger import logger


DEFAULT_LOGIN_URL = "https://q1espn-ms.qa1blue.ccvapor.net/account/index.html"


@dataclass(frozen=True)
class LoginSettings:
    login_url: str
    username: str
    password: str

    @classmethod
    @logger
    def from_sources(
        cls, username: str | None = None, password: str | None = None
    ) -> "LoginSettings":
        username = username or os.environ.get("PLAYWRIGHT_USERNAME")
        password = password or os.environ.get("PLAYWRIGHT_PASSWORD")

        missing = []
        if not username:
            missing.append("--username or PLAYWRIGHT_USERNAME")
        if not password:
            missing.append("--password or PLAYWRIGHT_PASSWORD")
        if missing:
            raise RuntimeError(f"Missing login credentials: {', '.join(missing)}.")

        return cls(
            login_url=os.environ.get("PLAYWRIGHT_LOGIN_URL", DEFAULT_LOGIN_URL),
            username=username,
            password=password,
        )