from typing import Optional, Union

from ..settings import CHILDREN_MAPPING


def children(string: Union[str, int]) -> Optional[int]:
    if string is None:
        return

    string = str(string).lower().strip()

    return CHILDREN_MAPPING.get(string, None)
