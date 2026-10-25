import re
from typing import Optional
from ..settings import IPV4_REGEX, IPV6_REGEX


def ip_address(
    string: str,
) -> Optional[str]:
    if not string:
        return

    string = string.strip()

    if not re.match(IPV4_REGEX, string) and not re.match(IPV6_REGEX, string):
        return

    return string
