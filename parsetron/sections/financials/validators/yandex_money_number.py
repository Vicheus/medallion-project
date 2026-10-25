from typing import Optional

from parsetron.sections.base.validators.base import base_validation


def yandex_money_number(string: str) -> Optional[str]:
    card_number = base_validation(string)

    if not card_number:
        return

    card_number = card_number.strip()
    if len(card_number) != 15:
        return

    return card_number
