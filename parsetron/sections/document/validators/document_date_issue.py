from typing import Optional

from parsetron.sections.base.validators.date import base_date_validation


def document_date_issue(string: str, date_format: str = "yyyy-MM-dd") -> Optional[str]:
    return base_date_validation(
        string, date_format, max_years_to=0, max_years_from=1020
    )
