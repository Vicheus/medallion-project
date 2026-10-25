from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, field_validator, Field, model_validator

from parsetron.engine.bronze.config import Bronze
from parsetron.engine.constants import SourceIdTypes, StageTypes
from parsetron.engine.gold.config import Gold
from parsetron.engine.silver.config import Silver
from parsetron.engine.utils.util import check_duplicates, check_set_equality


class PipelineConfig(BaseModel):
    source_id: str = Field(alias="sourceId")
    country_code: Literal["RU", "BY", "KZ"] = Field(None, alias="countryCode")
    source_entity_id_hash_type: str = Field(
        SourceIdTypes.SHA_HASH_ID.value, alias="sourceEntityIdHashType"
    )
    bronze: list[Bronze]
    silver: list[Silver]
    gold: Gold

    @model_validator(mode="after")
    def validate_layers_integrity(self):
        bronze_ids = [item.id for item in self.bronze if item.entities]
        if not bronze_ids and [item.id for item in self.bronze]:
            raise ValueError(
                f"At least one {StageTypes.BRONZE.name} must have entities"
            )
        silver_ids = [item.id for item in self.silver]
        gold_ids = [item.id for item in self.gold.ids] if self.gold.ids else [""]
        check_duplicates(bronze_ids, StageTypes.BRONZE.name)
        check_duplicates(silver_ids, StageTypes.SILVER.name)
        check_duplicates(gold_ids, StageTypes.GOLD.name)
        bronze_set = set(bronze_ids)
        silver_set = set(silver_ids)
        gold_set = set(gold_ids)
        check_set_equality(
            bronze_set, silver_set, StageTypes.BRONZE.name, StageTypes.SILVER.name
        )
        check_set_equality(
            silver_set, gold_set, StageTypes.SILVER.name, StageTypes.GOLD.name
        )
        return self

    @field_validator(StageTypes.BRONZE.value, StageTypes.SILVER.value, mode="before")
    @classmethod
    def ensure_list(cls, v):
        if isinstance(v, list):
            return v
        return [v]
