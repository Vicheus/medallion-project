from typing import Optional, Dict, Union, List
from parsetron.sections.base.validators.base import base_validation
from .incidence_date import incidence_date


def incidence(
    title: str = None,
    date: str = None,
    insurance: str = None,
    participants: List[str] = None,
    comment: str = None,
) -> Optional[Dict[str, Union[int, str]]]:
    title = base_validation(title)
    date = incidence_date(date)
    participants = [base_validation(x) for x in participants]
    if not title:
        return
    if (not date) & (not insurance) & (not participants):
        return

    return {
        "title": title,
        "date": date,
        "insurance": insurance,
        "participants": participants,
        "comment": comment,
    }
