from typing import Optional

from parsetron.sections.base.validators.date import base_date_validation


def birth_date(string: str, date_format: str = "%d.%m.%Y") -> Optional[str]:
    return base_date_validation(string, date_format, max_years_from=115, max_years_to=0)
