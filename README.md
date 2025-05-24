# Logger Project

This project provides a simple utility function to obtain ready-to-use
Python loggers. It is intended as a minimal template for projects that
require consistent logging without boilerplate configuration.

## Setup

1. Ensure that you have **Python 3.8+** installed.
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the development dependencies:
   ```bash
   pip install pytest
   ```

## Running Tests

Execute the unit tests with:

```bash
pytest
```

## Usage Example

```python
from src.logger import get_logger

logger = get_logger("example")
logger.info("Logger is ready to use!")
```

The `get_logger` function ensures that a basic configuration is set so
that the logger emits messages immediately.

