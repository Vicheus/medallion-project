from typing import Optional


def validate_type(string: str) -> Optional[str]:
    try:
        if not string:
            return
        sev = int(string)

        if not sev:
            return

        if sev not in [0, 1, 2, 3, 4]:
            return
        else:
            return sev
    except:  # noqa: E722
        return
