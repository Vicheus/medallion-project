import re

from typing import Optional
from ..settings import VALID_CARD_BINS
from typing import List


def financial_card_number(card_number: str) -> Optional[str]:
    def remove_non_numeric(s):
        return re.sub(r"\D", "", s)

    if not card_number:
        return

    card_number = card_number.strip()
    card_number = remove_non_numeric(card_number)
    if len(card_number) != 16:
        return

    bin_code = card_number[:6]
    if bin_code not in VALID_CARD_BINS:
        return

    return card_number


def financial_cards_numbers(cards_numbers: List[str]) -> Optional[List[str]]:
    if not cards_numbers:
        return None

    formatted_cards_numbers = set()
    for card_number in cards_numbers:
        formatted_card_number = financial_card_number(card_number)
        if not formatted_card_number:
            continue

        formatted_cards_numbers.add(formatted_card_number)

    return list(formatted_cards_numbers) if len(formatted_cards_numbers) > 0 else None
