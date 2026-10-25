from __future__ import annotations

from typing import ClassVar, Any, Optional

from pydantic import BaseModel, model_validator, ConfigDict, Field, field_validator
from pydantic_core.core_schema import ValidationInfo
from pyspark.sql import DataFrame

from parsetron.engine.registry.base import ActionType
from parsetron.engine.registry.functions.base import BaseAction


class BaseOperation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    op: str
    _registry: ClassVar[dict[str, type["BaseOperation"]]] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "apply" in cls.__dict__:
            fn = cls.__annotations__.get("op")
            if fn:
                BaseOperation._registry[str(fn)[16:-2]] = cls

    def apply(self, df: DataFrame) -> DataFrame:
        raise NotImplementedError

    @model_validator(mode="before")
    @classmethod
    def parse_nested(cls, values: Any, info: ValidationInfo):
        if isinstance(values, dict):
            for key, value in values.items():
                if isinstance(value, dict):
                    if "op" in value:
                        values[key] = BaseOperation.from_dict(value, info)
                    elif "fn" in value:
                        values[key] = BaseAction.from_dict(value, info)
                elif isinstance(value, list):
                    new_list = []
                    for item in value:
                        if isinstance(item, dict):
                            if "fn" in item:
                                new_list.append(BaseAction.from_dict(item, info))
                            else:
                                new_list.append(item)
                        else:
                            if "op" in value:
                                new_list.append(BaseOperation.from_dict(item, info))
                            elif "fn" in value:
                                new_list.append(BaseAction.from_dict(item, info))
                            else:
                                new_list.append(item)
                    values[key] = new_list
        return values

    @classmethod
    def from_dict(
        cls, data: dict[str, Any], info: Optional[ValidationInfo] = None
    ) -> "BaseOperation":
        fn = data["op"]
        instance = BaseOperation._registry.get(fn)
        if not instance:
            raise ValueError(f"Unknown op: {fn!r}")
        return instance.model_validate(data, context=info.context if info else {})


class BaseOpCols(BaseModel):
    columns: list[str] = Field(min_length=1)

    @field_validator("columns", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]


class ActionOpCols(BaseModel):
    columns: list[ActionType] = Field(min_length=1)

    @field_validator("columns", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if not isinstance(v, list):
            return v
        return [v]
