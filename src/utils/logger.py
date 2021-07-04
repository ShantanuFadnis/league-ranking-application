"""Logger Module"""
import logging
from typing import Any

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


def init_logging_object(name: str = None) -> Any:  # type:ignore
    """
    Customer logger to use in any module within this application
    @param name: str - Name of module using this logger

    @return: Any
    """
    logger = logging.getLogger(name)
    return logger
