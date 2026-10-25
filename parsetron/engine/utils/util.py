def check_duplicates(ids: list, name: str) -> None:
    seen = set()
    duplicates = set()
    for x in ids:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    if duplicates:
        raise ValueError(f"Duplicate IDs found in {name}: {duplicates}")


def check_set_equality(set_a: set, set_b: set, name_a: str, name_b: str) -> None:
    if set_a != set_b:
        diff_a = set_a - set_b
        diff_b = set_b - set_a
        error_msg = f"Mismatch between {name_a} and {name_b}:"
        parts = []
        if diff_a:
            parts.append(f"{name_a} has extra IDs: {diff_a}")
        if diff_b:
            parts.append(f"{name_b} has extra IDs: {diff_b}")
        raise ValueError(f"{error_msg} {' | '.join(parts)}")
