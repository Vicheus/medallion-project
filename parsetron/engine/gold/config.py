from pydantic import BaseModel, model_validator, Field, ConfigDict
from pydantic_core.core_schema import ValidationInfo

from parsetron.engine.config.common import IO, IOParams
from parsetron.engine.registry.functions.base import BaseAction
from parsetron.engine.registry.transformations.base import BaseOperation


class EntityId(BaseModel):
    id: str
    transformations: list[BaseOperation] = []

    @model_validator(mode="before")
    @classmethod
    def parse_items(cls, values: dict, info: ValidationInfo):
        itms = values.get("transformations")
        if isinstance(itms, dict):
            itms = [itms]
        if isinstance(itms, list):
            operations = []
            for itm in itms:
                if isinstance(itm, dict):
                    operations.append(BaseOperation.from_dict(itm, info))
            values["transformations"] = operations
        return values


class Gold(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ignore_hash_error: bool = Field(False, alias="ignoreHashError")
    ids: list[EntityId] = Field(None, min_length=1)
    io: IO = IO(write=IOParams(type="coalesce", count=1))
    transformations: list[BaseOperation] = []
    remain: list[str] | BaseAction

    @model_validator(mode="before")
    @classmethod
    def parse_items(cls, values: dict, info: ValidationInfo):
        itms = values.get("transformations")
        if isinstance(itms, dict):
            itms = [itms]
        if isinstance(itms, list):
            operations = []
            for itm in itms:
                if isinstance(itm, dict):
                    operations.append(BaseOperation.from_dict(itm, info))
            values["transformations"] = operations
        itm = values.get("remain")
        if isinstance(itm, dict):
            values["remain"] = BaseAction.from_dict(itm, info)
        elif isinstance(itm, str):
            values["remain"] = [itm]
        return values
