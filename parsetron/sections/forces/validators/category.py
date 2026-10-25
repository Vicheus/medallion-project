from typing import Optional
from ..settings import FORCES_CATEGORY_MAPPING


def validate_category(value: Optional[str]) -> Optional[int]:
    if not value:
        return None
    value = str(value).lower().strip()
    return FORCES_CATEGORY_MAPPING.get(value, None)
