from __future__ import annotations

from typing import ClassVar, Any, Optional

from pydantic import BaseModel, model_validator, ConfigDict
from pydantic_core.core_schema import ValidationInfo
from pyspark.sql import DataFrame


class BaseBatchAction(BaseModel):
    model_config = ConfigDict(extra="forbid")
    batch_fn: str
    _registry: ClassVar[dict[str, type["BaseBatchAction"]]] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if "apply" in cls.__dict__:
            batch_fn = cls.__annotations__.get("batch_fn")
            if batch_fn:
                BaseBatchAction._registry[str(batch_fn)[16:-2]] = cls

    def apply(self, df: DataFrame, target_col: str) -> DataFrame:
        raise NotImplementedError

    @model_validator(mode="before")
    @classmethod
    def parse_nested(cls, values: Any, info: ValidationInfo):
        if isinstance(values, dict):
            for key, value in values.items():
                if isinstance(value, dict) and "batch_fn" in value:
                    values[key] = BaseBatchAction.from_dict(value, info)
                elif isinstance(value, list):
                    new_list = []
                    for item in value:
                        if isinstance(item, dict) and "batch_fn" in item:
                            new_list.append(BaseBatchAction.from_dict(item, info))
                        else:
                            new_list.append(item)
                    values[key] = new_list
        return values

    @classmethod
    def from_dict(
        cls, data: dict[str, Any], info: Optional[ValidationInfo] = None
    ) -> "BaseBatchAction":
        fn = data["batch_fn"]
        instance = BaseBatchAction._registry.get(fn)
        if not instance:
            raise ValueError(f"Unknown DF function: {fn!r}")
        return instance.model_validate(data, context=info.context if info else {})
