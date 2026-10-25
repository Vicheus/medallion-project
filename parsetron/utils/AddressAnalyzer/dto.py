from typing import Optional

from pydantic import BaseModel


class FetchDto(BaseModel):
    raw: str
    extended_raw: Optional[str]
    prepared_parts: dict = {}
    address_type: Optional[int] = None
    is_api_call_required: Optional[bool] = None
    response: Optional[dict] = None
