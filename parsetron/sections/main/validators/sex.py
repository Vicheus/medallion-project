from typing import Optional, Union

from ..settings import SEX_MAPPING


def sex(string: Union[str, int]) -> Optional[int]:
    if string is None:
        return

    string = str(string).lower().strip()

    return SEX_MAPPING.get(string, None)
