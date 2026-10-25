import logging
import os
import sys


def setup_logger(filename: str = "run.log"):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.getLogger("py4j").setLevel(logging.WARNING)

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)

    # File handler
    os.makedirs("logs", exist_ok=True)
    fh = logging.FileHandler(f"logs/{filename}")
    fh.setLevel(logging.DEBUG)

    # Formatter
    console_formatter = logging.Formatter(
        "%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )
    ch.setFormatter(console_formatter)

    file_formatter = logging.Formatter(
        "%(asctime)s.%(msecs)03d - %(levelname)s - %(name)s::%(funcName)s::%(lineno)d - %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S",
    )
    fh.setFormatter(file_formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
