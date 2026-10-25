from typing import Literal, Optional

from pydantic import BaseModel


class IOParams(BaseModel):
    type: Literal["repartition", "coalesce", "coalesce_size"] = "coalesce"
    count: int = 1


class IO(BaseModel):
    write: Optional[IOParams]
