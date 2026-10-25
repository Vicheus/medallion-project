from typing import Union, Optional

from pydantic import BaseModel, model_validator, ConfigDict, field_validator
from pydantic_core.core_schema import ValidationInfo

from parsetron.engine.config.common import IO, IOParams
from parsetron.engine.registry.base import ActionType
from parsetron.engine.registry.complex.functions.base import BaseBatchAction
from parsetron.engine.registry.functions.base import BaseAction


class SilverCol(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: Union[ActionType, BaseBatchAction]
    filter: Optional[Union[BaseAction, bool]] = None

    @model_validator(mode="before")
    @classmethod
    def parse_items(cls, values: dict, info: ValidationInfo):
        itm = values.get("source")
        if isinstance(itm, dict):
            if "batch_fn" in itm:
                values["source"] = BaseBatchAction.from_dict(itm, info)
            else:
                values["source"] = BaseAction.from_dict(itm, info)
        itm = values.get("filter")
        if isinstance(itm, dict):
            values["filter"] = BaseAction.from_dict(itm, info)
        return values


class SilverEntity(BaseModel):
    io: IO = IO(write=IOParams(count=3, type="repartition"))
    entities: list[str] = []
    columns: dict[str, SilverCol]

    @field_validator("entities", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]


class Silver(BaseModel):
    id: str = ""
    entities: dict[str, SilverEntity]
