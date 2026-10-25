from typing import Optional, Union

from ..settings import RELATIONSHIP_MAPPING


def relationship(string: Union[str, int]) -> Optional[int]:
    if string is None:
        return

    string = str(string).lower().strip()

    return RELATIONSHIP_MAPPING.get(string, None)
