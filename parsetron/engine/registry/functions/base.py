from __future__ import annotations

from typing import ClassVar, Any, Optional

from pydantic import BaseModel, model_validator, ConfigDict
from pydantic_core.core_schema import ValidationInfo
from pyspark.sql import Column


class BaseAction(BaseModel):
    model_config = ConfigDict(extra="forbid")
    fn: str
    _registry: ClassVar[dict[str, type["BaseAction"]]] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "apply" in cls.__dict__:
            fn = cls.__annotations__.get("fn")
            if fn:
                BaseAction._registry[str(fn)[16:-2]] = cls

    def apply(self) -> Column:
        raise NotImplementedError

    @model_validator(mode="before")
    @classmethod
    def parse_nested(cls, values: Any, info: ValidationInfo):
        if isinstance(values, dict):
            for key, value in values.items():
                if isinstance(value, dict) and "fn" in value:
                    values[key] = BaseAction.from_dict(value, info)
                elif isinstance(value, list):
                    new_list = []
                    for item in value:
                        if isinstance(item, dict) and "fn" in item:
                            new_list.append(BaseAction.from_dict(item, info))
                        else:
                            new_list.append(item)
                    values[key] = new_list
        return values

    @classmethod
    def from_dict(
        cls, data: dict[str, Any], info: Optional[ValidationInfo] = None
    ) -> "BaseAction":
        fn = data["fn"]
        instance = BaseAction._registry.get(fn)
        if not instance:
            raise ValueError(f"Unknown fn: {fn!r}")
        return instance.model_validate(data, context=info.context if info else {})
