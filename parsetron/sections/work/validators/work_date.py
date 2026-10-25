from typing import Optional
from parsetron.sections.base.validators.date import base_date_validation


def work_date(string: str, date_format: Optional[str] = "%Y-%m-%d") -> Optional[str]:
    return base_date_validation(string, date_format)
