from typing import Optional, Dict, Union

from parsetron.sections.base.validators.base import (
    base_validation,
    is_ukrainian_symbols,
)


def link(
    title: str, link: str, comment: Optional[str] = None
) -> Optional[Dict[str, Union[str, None]]]:
    if not link or not "/" in link:
        print(f"Invalid link provided: {link}")
        return None
    cleaned_title = base_validation(title)
    if not cleaned_title:
        if title != "X":
            return None
        cleaned_title = "X"

    if is_ukrainian_symbols(link):
        return None
    cleaned_link = link.strip()
    if not cleaned_link or len(cleaned_link) < 6:
        return None
    if len(cleaned_link) > 350:
        cleaned_link = cleaned_link[:350]
    cleaned_comment = base_validation(comment)

    return {
        "title": cleaned_title,
        "link": cleaned_link,
        "comment": cleaned_comment,
    }
