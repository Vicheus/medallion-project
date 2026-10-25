from typing import Optional
from math import pow
import hashlib
import re


def sha1_hash(card_number):
    return hashlib.sha1(card_number.encode("utf-8")).hexdigest().upper()


HASH_TYPES = {"sha1": sha1_hash}


def brute_force_card(
    card_number_masked: str,
    card_hash: str,
    hash_type: str,
    numbers_to_brute_force: int,
    symbol_to_replace: str,
) -> Optional[str]:
    hash_algorithm = HASH_TYPES[hash_type]
    if not hash_algorithm:
        return None

    for i in range(int(pow(10, numbers_to_brute_force))):
        middle_part = str(i).zfill(numbers_to_brute_force)
        card_number_full = card_number_masked.replace(
            symbol_to_replace * numbers_to_brute_force, middle_part
        )
        if hash_algorithm(card_number_full) == card_hash:
            return card_number_full


def extract_invoice_number_for_physical_person(text: str):
    if not text:
        return None
    pattern = r"\b408\d{17}\b"

    match = re.search(pattern, text)
    first_match = match.group(0) if match else None

    return first_match
