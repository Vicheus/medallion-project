from typing import Optional, Dict, Union

from parsetron.sections.base.validators.base import base_validation
from ..settings import Titles


def social(
    title: str, id: str = None, link: str = None, comment: str = None
) -> Optional[Dict[str, Union[int, str]]]:
    if not title:
        return

    if id:
        id = base_validation(id)

    if (not id) & (not link):
        return

    if (title == Titles.Telegram) and id:
        try:
            if len(id) < 9 or len(id) > 10:
                return
        except ValueError:
            return

    return {
        "title": base_validation(title),
        "id": id,
        "link": link,
        "comment": base_validation(comment),
    }
