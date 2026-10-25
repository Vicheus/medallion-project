from typing import Optional
from ..settings import EDUCATION_LEVEL_MAPPING


def education_level(level: str) -> Optional[int]:
    if not level:
        return None
    level = level.strip().lower()

    mapped_level = EDUCATION_LEVEL_MAPPING.get(level)

    return mapped_level
