def split_by(value: str, by: str = ",") -> list[str]:
    values = value.split(by) if value else []
    values = [v.strip().lower() for v in values]
    return values
