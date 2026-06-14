import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)


def setup_logging() -> None:
    formatter = logging.Formatter(LOG_FORMAT)

    app_handler = RotatingFileHandler(
        LOG_DIR / "app.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
    )

    error_handler = RotatingFileHandler(
        LOG_DIR / "error.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
    )

    console_handler = logging.StreamHandler()

    app_handler.setFormatter(formatter)
    error_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    app_handler.setLevel(logging.INFO)
    error_handler.setLevel(logging.ERROR)
    console_handler.setLevel(logging.INFO)

    root_logger = logging.getLogger()

    root_logger.setLevel(logging.INFO)

    root_logger.addHandler(app_handler)
    root_logger.addHandler(error_handler)
    root_logger.addHandler(console_handler)