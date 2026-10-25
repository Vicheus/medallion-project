import logging
import sys
import time
from functools import wraps
from logging import Logger
from typing import Optional


def track_execution_time(logger: logging.Logger, name: Optional[str] = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            display_name = name or func.__name__
            mins = (time.perf_counter() - start) / 60
            logger.info(f"{display_name} executed in {mins:.2f} m")
            return result

        return wrapper

    return decorator


def track_execution_entity_time(
    logger: logging.Logger, job_type: str, entity: str, func
) -> None:
    start = time.perf_counter()
    logger.info(f"Started {job_type} job for entity {entity}")
    func()
    mins = (time.perf_counter() - start) / 60
    logger.info(f"Completed {job_type} job for entity {entity} in {mins:.2f} m")


def track_start_command(logger: Logger):
    command = " ".join(sys.argv)
    logger.info(f"Start command: {command}")
