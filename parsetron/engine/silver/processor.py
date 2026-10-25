from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from parsetron.engine.constants import ColumnTypes
from parsetron.engine.registry.complex.functions.base import BaseBatchAction
from parsetron.engine.registry.resolver import resolve
from parsetron.engine.silver.config import SilverCol


class Processor:
    def process(self, df: DataFrame, columns: dict[str, SilverCol]) -> DataFrame:
        for target_col, cfg in columns.items():
            if isinstance(cfg.source, BaseBatchAction):
                df = cfg.source.apply(df, target_col)
            else:
                df = df.withColumn(target_col, resolve(cfg.source))
            if cfg.filter:
                if isinstance(cfg.filter, bool):
                    df = df.filter(col(target_col).isNotNull())
                else:
                    df = df.filter(resolve(cfg.filter))

        select_cols = [key for key in columns.keys() if not key.startswith("__")]
        return df.select(ColumnTypes.SOURCE_ENTITY_ID.value, *select_cols)
