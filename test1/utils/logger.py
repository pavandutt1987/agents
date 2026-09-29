import logging
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")


def logger(function: Callable[P, R]) -> Callable[P, R]:
    function_logger = logging.getLogger(function.__module__)

    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        function_logger.info("Starting %s", function.__qualname__)
        try:
            result = function(*args, **kwargs)
        except Exception:
            function_logger.exception("Failed %s", function.__qualname__)
            raise
        function_logger.info("Completed %s", function.__qualname__)
        return result

    return wrapper