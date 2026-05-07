import logging
import os
from logging.handlers import RotatingFileHandler


def configure_logging():
    """
    Configure the root logger with a StreamHandler and optional RotatingFileHandler.

    Environment variables:
      - LOG_FILE: path to write log file (default: /var/log/market/market.log)
      - LOG_LEVEL: logging level (default: INFO)

    Idempotent: returns immediately if handlers already configured.
    """
    log_file = os.getenv("LOG_FILE", "/var/log/market/market.log")
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    root = logging.getLogger()
    if root.handlers:
        return

    root.setLevel(level)
    fmt = "%(asctime)s %(levelname)s %(name)s %(message)s"
    formatter = logging.Formatter(fmt)

    # Stream handler (stdout)
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    root.addHandler(sh)

    # Optional rotating file handler
    try:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
        fh = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
        fh.setFormatter(formatter)
        root.addHandler(fh)
    except Exception:
        root.exception("Failed to create file handler for %s", log_file)
