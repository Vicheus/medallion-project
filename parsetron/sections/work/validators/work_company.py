from typing import Optional, List

from parsetron.sections.base.validators.base import base_validation


def work_company(string: str) -> Optional[List[str]]:
    string = base_validation(string)

    if not string:
        return

    if len(string) <= 2:
        return

    return string
