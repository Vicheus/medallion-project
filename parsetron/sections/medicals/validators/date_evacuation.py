from typing import Optional
from parsetron.sections.base.validators.date import base_date_validation


def validate_date_evacuation(
    string: str, date_format: Optional[str] = "%Y-%m-%d"
) -> Optional[str]:
    return base_date_validation(string, date_format, max_years_from=100)
