from typing import Optional, List

from parsetron.sections.base.validators.base import base_validation


def relation(string: str) -> Optional[List[str]]:
    string = base_validation(string)

    if not string:
        return

    return string
