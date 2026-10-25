from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, field_validator, Field, ConfigDict, model_validator
from pydantic_core.core_schema import ValidationInfo

from parsetron.engine.config.common import IO, IOParams
from parsetron.engine.constants import JoinTypes
from parsetron.engine.registry.functions.base import BaseAction


class BronzeAppend(BaseModel):
    append: list[BronzeJoin | BronzeUnion] = []

    @field_validator("append", mode="before")
    @classmethod
    def ensure_append_is_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]


class BronzeRead(BronzeAppend):
    model_config = ConfigDict(extra="forbid")
    format: Literal["csv"] = "csv"
    base_path: str = Field("", alias="basePath")
    path: str
    header: list[str] = []
    options: dict = {}
    trim_values: bool | str = Field(False, alias="trimValues")
    replace_regex_patrial: dict[str, str] = Field({}, alias="replaceRegexPatrial")
    replace_with_none: list[str] = Field([], alias="replaceWithNone")
    replace_regex_with_none: list[str] = Field([], alias="replaceRegexWithNone")
    aliases: dict[str, str] = {}
    filter: Optional[BaseAction] = None

    @model_validator(mode="before")
    @classmethod
    def parse_items(cls, values: dict, info: ValidationInfo):
        itm = values.get("filter")
        if isinstance(itm, dict):
            values["filter"] = BaseAction.from_dict(itm, info)
        return values

    @field_validator("replace_with_none", "replace_regex_with_none", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]

    @field_validator("aliases", mode="before")
    @classmethod
    def update_aliases(cls, v):
        if not isinstance(v, dict):
            return v
        data = {}
        for key, value in v.items():
            data[key.replace(".", "_").strip()] = value
        return data


class BronzeJoin(BronzeAppend):
    model_config = ConfigDict(extra="forbid")
    read: BronzeRead
    ids: list[str] = Field(min_length=1)
    how: Literal["inner", "left", "right", "outer", "left_anti", "full"] = Field(
        JoinTypes.LEFT.value, alias="type"
    )
    rename_suffix: str = Field(None, alias="renameSuffix")

    @field_validator("ids", mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]


class BronzeUnion(BronzeAppend):
    model_config = ConfigDict(extra="forbid")
    read: BronzeRead
    allow_missing_columns: bool = Field(False, alias="allowMissingColumns")


class BronzeSourceCol(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str
    type: Literal["string", "timestamp", "integer", "double"] = "string"

    @model_validator(mode="after")
    def clean_source(self):
        if "." in self.source:
            self.source = self.source.replace(".", "_")
        return self


class BronzeEntity(BaseModel):
    model_config = ConfigDict(extra="forbid")
    io: IO = IO(write=IOParams(count=4, type="repartition"))
    columns: dict[str, BronzeSourceCol | str]

    @model_validator(mode="after")
    def clean_column_source(self):
        for key, value in self.columns.items():
            if isinstance(value, str) and "." in value:
                self.columns[key] = value.replace(".", "_")
        return self


class BronzeAfterRead(BaseModel):
    model_config = ConfigDict(extra="forbid")
    distinct: bool = True
    cache: bool = True


class Bronze(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str = ""
    read: BronzeRead
    after_read: BronzeAfterRead = Field(BronzeAfterRead(), alias="afterRead")
    entities: dict[str, BronzeEntity] = {}
