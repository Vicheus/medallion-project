import re
from typing import Optional


def clean_doc_serial(value: str) -> Optional[str]:
    pattern = re.compile(r"[^A-Za-zА-ЯЁа-яё0-9]")
    return pattern.sub("", value)


def is_doc_length_valid(value: str) -> bool:
    if not value:
        return False
    if len(value) <= 4 and len(set(value)) <= 1:
        return False
    return True


def document_serial(value: str) -> Optional[str]:
    if not value:
        return None

    value = clean_doc_serial(value)
    if not is_doc_length_valid(value):
        return None

    digits = value
    if not value.isdigit():
        digits = re.sub(r"\D", "", value)

    if check_sequential_or_repeated_patterns(digits):
        return None

    return value


def document_serial_digits(value: str) -> Optional[str]:
    if not value:
        return None

    value = clean_doc_serial(value)
    if not is_doc_length_valid(value) or not value.isdigit():
        return None
    if check_sequential_or_repeated_patterns(value):
        return None
    return value


def check_sequential_or_repeated_patterns(number: str) -> bool:
    if not number:
        return True

    length = len(number)
    min_seq_len = 5

    # Enough repeated digits (000000)
    if all(d == number[0] for d in number):
        return True

    # Repeated patterns (121212, 123123)
    for size in range(1, length // 2 + 1):
        pattern = number[:size]
        if pattern * (length // size) == number:
            return True

    # Ascending and descending digit sequences
    asc = "0123456789012345678901234567890123456789"
    desc = "9876543210987654321098765432109876543210"

    # Check all substrings of length >= min_seq_len
    for size in range(min_seq_len, length + 1):
        for i in range(length - size + 1):
            sub = number[i : i + size]
            if sub in asc or sub in desc:
                return True

    # Extra: check if number starts with a long sequence (12345678901)
    for seq in [asc, desc]:
        for i in range(len(seq) - min_seq_len):
            pattern = seq[i : i + min_seq_len]
            if number.startswith(pattern):
                return True

    return False


def match_pattern(pattern: str, value: str) -> Optional[re.Match[str]]:
    if value:
        return re.search(pattern, value)
    return None


def extract_pattern(pattern: str, value: str) -> Optional[str]:
    match = match_pattern(pattern, value)
    if match:
        return match.group(1)
    return None
