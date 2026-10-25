from typing import Optional


def validate_severity(string: str) -> Optional[str]:
    try:
        if not string:
            return
        sev = int(string)

        if not sev:
            return

        if sev not in [1, 2, 3, 4, 5]:
            return
        else:
            return sev
    except:  # noqa: E722
        return
