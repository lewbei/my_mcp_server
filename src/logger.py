import logging

def get_logger(name: str) -> logging.Logger:
    """Return a configured logger with the given name.

    The logger is configured with a basic configuration if not already
    configured. This allows immediate use without additional setup.
    """
    if not logging.getLogger().hasHandlers():
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    return logging.getLogger(name)
