import logging
import os
from datetime import datetime
from config import Config


def get_logger(name):
    os.makedirs(Config.LOG_DIR, exist_ok=True)
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    console = logging.StreamHandler()
    console.setFormatter(fmt)

    file = logging.FileHandler(
        os.path.join(Config.LOG_DIR, f"test_run_{datetime.now().strftime('%Y%m%d')}.log")
    )
    file.setFormatter(fmt)

    logger.addHandler(console)
    logger.addHandler(file)
    return logger