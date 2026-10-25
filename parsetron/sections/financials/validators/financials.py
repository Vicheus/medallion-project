from typing import Optional, Dict, Union
from .financial_date_expire import financial_date_expire
from .financial_date_issue import financial_date_issue
from .financial_card_number import financial_card_number
from .financial_invoice_number import financial_invoice_number


def financial(
    title: str = None,
    card_number: str = None,
    invoice_number: str = None,
    date_issue: str = None,
    date_expire: str = None,
    comment: str = None,
    date_format: str = "yyyy-MM-dd",
) -> Optional[Dict[str, Union[int, str]]]:
    card_number = financial_card_number(card_number)
    invoice_number = financial_invoice_number(invoice_number)
    date_issue = financial_date_issue(date_issue, date_format)
    date_expire = financial_date_expire(date_expire, date_format)

    return {
        "title": title,
        "card_number": card_number,
        "invoice_number": invoice_number,
        "date_issue": date_issue,
        "date_expire": date_expire,
        "comment": comment,
    }
