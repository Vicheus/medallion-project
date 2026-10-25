from datetime import date


def get_current_iso_date() -> str:
    return date.today().isoformat()
