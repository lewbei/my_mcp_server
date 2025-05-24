import logging
import pytest

from src.logger import get_logger


def test_get_logger_returns_logger_with_name():
    name = "my_test_logger"
    logger = get_logger(name)
    assert isinstance(logger, logging.Logger)
    assert logger.name == name
