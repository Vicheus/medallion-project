from pyspark.sql import Column, DataFrame, Window
from pyspark.sql.functions import (
    coalesce,
    col,
    concat_ws,
    lit,
    monotonically_increasing_id,
    row_number,
    sha2,
    xxhash64,
)

from parsetron.engine.constants import ColumnTypes


def concat_values(values: Column) -> Column:
    return concat_ws("||", values)


def _sort_and_concat(columns: list[str]) -> Column:
    sorted_columns = sorted(columns)
    values = (coalesce(col(c).cast("string"), lit("NULL")) for c in sorted_columns)
    return concat_ws("||", *values)


def add_row_number_id(df: DataFrame) -> DataFrame:
    sorted_key_name = "_sorted_value_key"
    window_spec = Window.orderBy(sorted_key_name)
    partitions = df.rdd.getNumPartitions()
    df = df.withColumn(sorted_key_name, _sort_and_concat(df.columns))
    df = df.withColumn(
        ColumnTypes.SOURCE_ENTITY_ID.value, row_number().over(window_spec)
    )
    return df.drop(sorted_key_name).repartition(partitions)


def hash_xxhash64(column: Column) -> Column:
    return xxhash64(column)


def add_xxhash64_id(df: DataFrame) -> DataFrame:
    return df.withColumn(
        ColumnTypes.SOURCE_ENTITY_ID.value,
        hash_xxhash64(_sort_and_concat(df.columns)),
    )


def hash_sha224(column: Column) -> Column:
    return sha2(column, 224)


def add_sha224_id(df: DataFrame) -> DataFrame:
    return df.withColumn(
        ColumnTypes.SOURCE_ENTITY_ID.value,
        hash_sha224(_sort_and_concat(df.columns)),
    )


def add_monotonically_increasing_id(df: DataFrame) -> DataFrame:
    return df.withColumn(
        ColumnTypes.SOURCE_ENTITY_ID.value, monotonically_increasing_id()
    )
