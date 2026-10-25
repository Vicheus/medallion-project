from typing import Optional

from parsetron.sections.base.validators.base import base_validation


def financial_invoice_number(string: str) -> Optional[str]:
    invoice_number = base_validation(string)

    if not invoice_number:
        return

    invoice_number = invoice_number.strip()
    if len(invoice_number) != 20:
        return

    return invoice_number
