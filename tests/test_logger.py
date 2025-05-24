import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import logging
import pytest

from src.logger import get_logger


def test_get_logger_returns_logger_with_name():
    name = "my_test_logger"
    logger = get_logger(name)
    assert isinstance(logger, logging.Logger)
    assert logger.name == name
