import yaml

from parsetron.engine.config.base import PipelineConfig
from parsetron.engine.registry.functions.conditions import AndFn
from parsetron.engine.registry.functions.custom import CasesFn
from parsetron.engine.registry.functions.modifiers import ArrayFn
from parsetron.engine.registry.functions.udfs import ActualityDateUdf
from parsetron.engine.registry.transformations.basic import FilterOp
from parsetron.engine.registry.transformations.group import GroupByOp
from parsetron.engine.registry.transformations.columns import RelationsOp
from parsetron.engine.registry.complex.functions.address import StructuredAddressBatchFn


def load_source_config(path: str) -> PipelineConfig:
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return PipelineConfig.model_validate(
        config, context={"country_code": config.get("countryCode")}
    )
