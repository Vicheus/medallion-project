import re
from typing import Optional, List

from ..settings import EMAIL_REGEX, STOP_WORDS_EMAIL, STOP_DOMAINS_EMAIL


def email(string: str) -> Optional[str]:
    if not string:
        return

    string = string.strip().lower()

    if not re.match(EMAIL_REGEX, string):
        return

    username, domain = string.split("@")

    if username in STOP_WORDS_EMAIL or domain in STOP_DOMAINS_EMAIL:
        return

    if any(word in STOP_WORDS_EMAIL for word in domain.split(".")):
        return

    return string


def emails(emails: List[str]) -> Optional[List[str]]:
    if not emails:
        return None

    formatted_emails = set()
    for email_value in emails:
        formatted_email = email(email_value)
        if not formatted_email:
            continue

        formatted_emails.add(formatted_email)

    return list(formatted_emails) if len(formatted_emails) > 0 else None
