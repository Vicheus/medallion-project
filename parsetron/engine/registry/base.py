from __future__ import annotations

from pydantic import BaseModel, Field, field_validator, ConfigDict

from parsetron.engine.registry.functions.base import BaseAction


class ColLiteral(BaseModel):
    model_config = ConfigDict(extra="forbid")
    lit: str | int | float | list | None


ActionType = BaseAction | ColLiteral | str
ActionLitType = BaseAction | ColLiteral | str


class BaseCol(BaseModel):
    column: ActionType


class BaseCols(BaseModel):
    columns: list[ActionType] = Field(min_length=1)

    @field_validator("columns", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]


class BaseValue(BaseModel):
    value: ActionLitType
