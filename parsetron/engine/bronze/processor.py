import logging
from functools import singledispatch

from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import col, lit
from pyspark.sql.types import StringType, TimestampType, IntegerType, DoubleType

from parsetron.engine.bronze.config import BronzeSourceCol
from parsetron.engine.constants import ColumnTypes

logger = logging.getLogger(__name__)


TYPE_MAP = {
    "double": DoubleType(),
    "integer": IntegerType(),
    "string": StringType(),
    "timestamp": TimestampType(),
}


@singledispatch
def _prepare_column(value: str, columns: list[str]) -> Column:
    if value in columns:
        col_expr = col(value).cast(StringType())
    else:
        col_expr = lit(None).cast(StringType())
    return col_expr


@_prepare_column.register(BronzeSourceCol)
def _(value: BronzeSourceCol, columns: list[str]) -> Column:
    spark_type = TYPE_MAP.get(value.type)
    if not spark_type:
        raise ValueError(f"Unsupported type: {value.type}")
    if value.source in columns:
        col_expr = col(value.source).cast(spark_type)
    else:
        col_expr = lit(None).cast(spark_type)
    return col_expr


def _extract_entity(
    df: DataFrame, columns: dict[str, BronzeSourceCol | str]
) -> DataFrame:
    select_exprs = [col(ColumnTypes.SOURCE_ENTITY_ID.value)]
    df_columns = df.columns

    for column, config in columns.items():
        select_exprs.append(_prepare_column(config, df_columns).alias(column))

    df = df.select(*select_exprs)
    columns_to_filter = [
        column for column in df.columns if column != ColumnTypes.SOURCE_ENTITY_ID.value
    ]
    return df.dropna(how="all", subset=columns_to_filter)


class Processor:
    def process(
        self, df: DataFrame, columns: dict[str, BronzeSourceCol | str]
    ) -> DataFrame:
        return _extract_entity(df, columns)
