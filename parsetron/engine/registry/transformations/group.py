import logging
from functools import singledispatch
from typing import Literal
from typing import Optional

from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import (
    array,
    array_compact,
    array_distinct,
    array_sort,
    col,
    collect_set,
    first,
    flatten,
    lit,
    max,
    raise_error,
    size,
    struct,
    when,
)

from parsetron.engine.constants import (
    ColumnAggTypes,
    ColumnTypes,
    SourceIdTypes,
    TempColumnNames,
)
from parsetron.engine.registry.functions.base import BaseAction
from parsetron.engine.registry.resolver import resolve_expr
from parsetron.engine.registry.transformations.base import BaseOperation, BaseOpCols
from parsetron.engine.utils.generator.id import hash_sha224, hash_xxhash64

logger = logging.getLogger(__name__)

HASH_FUNC_MAP = {
    SourceIdTypes.NUM_HASH_ID.value: hash_xxhash64,
    "DEFAULT": hash_sha224,
}


def _define_simple_agg_col(column: str) -> Optional[Column]:
    if column in ColumnAggTypes.MAX.value:
        return max(col(column)).alias(column)
    if column in ColumnAggTypes.ANY.value:
        return (
            when(
                size(collect_set(col(column))) > 1,
                raise_error(
                    lit(
                        f"Multiple values found for {column} during groupBy transformation"
                    )
                ),
            )
            .otherwise(first(col(column), ignorenulls=True))
            .alias(column)
        )

    return None


def _define_group_agg_col(column: str) -> Column:
    expr = _define_simple_agg_col(column)
    if expr is not None:
        return expr
    return array_sort(
        array_compact(array_distinct(flatten(collect_set(col(column)))))
    ).alias(column)


def _find_source_entity_id_type(col_types: list[tuple[str, str]]) -> Optional[str]:
    for col_name, col_type in col_types:
        if col_name == ColumnTypes.SOURCE_ENTITY_ID.value:
            return col_type
    return None


def _define_source_id_col(col_types: list[tuple[str, str]]) -> Column:
    if _find_source_entity_id_type(col_types) != "array<string>":
        return array_sort(collect_set(col(ColumnTypes.SOURCE_ENTITY_ID.value))).alias(
            ColumnTypes.SOURCE_ENTITY_ID.value
        )
    return array_sort(
        array_compact(
            array_distinct(
                flatten(collect_set(col(ColumnTypes.SOURCE_ENTITY_ID.value)))
            )
        )
    ).alias(ColumnTypes.SOURCE_ENTITY_ID.value)


def _define_agg_col(column: str, df: DataFrame):
    if column == ColumnTypes.SOURCE_ENTITY_ID.value:
        return _define_source_id_col(df.dtypes)
    return _define_group_agg_col(column)


@singledispatch
def _get_negative_condition(expr: str) -> str:
    return f"NOT ({expr})"


@_get_negative_condition.register(Column)
def _(expr: Column) -> Column:
    return ~expr


def _group_by(
    df: DataFrame,
    group_by_cols: list[str],
    agg_cols: list[Column],
    positive: Optional[BaseAction | str],
    negative: Optional[BaseAction | bool | str],
) -> DataFrame:
    if positive:
        positive = resolve_expr(positive)
        full_df = df.filter(positive)
        result_df = full_df.groupBy(group_by_cols).agg(*agg_cols)
        if negative:
            if isinstance(negative, bool):
                negative = _get_negative_condition(positive)
            else:
                negative = resolve_expr(negative)
            null_df = df.filter(negative)
            # TODO: Handle type mismatch
            if _find_source_entity_id_type(null_df.dtypes) != "array<string>":
                null_df = null_df.withColumn(
                    ColumnTypes.SOURCE_ENTITY_ID.value,
                    array(col(ColumnTypes.SOURCE_ENTITY_ID.value)),
                )
            result_df = result_df.unionByName(null_df)
    else:
        result_df = df.groupBy(group_by_cols).agg(*agg_cols)

    return result_df


class GroupByOp(BaseOperation, BaseOpCols):
    op: Literal["groupBy"]
    positive: Optional[BaseAction | str] = None
    negative: Optional[BaseAction | bool | str] = True

    def apply(self, df: DataFrame) -> DataFrame:
        columns = df.columns
        agg_cols = [
            _define_agg_col(column, df)
            for column in columns
            if column not in self.columns
        ]
        return _group_by(df, self.columns, agg_cols, self.positive, self.negative)


class AggGroupByOp(BaseOperation, BaseOpCols):
    op: Literal["aggGroupBy"]
    columns: list[str] = [ColumnTypes.SOURCE_ENTITY_ID.value]
    positive: Optional[BaseAction | str] = None
    negative: Optional[BaseAction | bool | str] = True

    def apply(self, df: DataFrame) -> DataFrame:
        columns = df.columns
        group_by_cols = [column for column in columns if column not in self.columns]
        agg_cols = [_define_agg_col(column, df) for column in self.columns]
        return _group_by(df, group_by_cols, agg_cols, self.positive, self.negative)


class ActualityGroupByOp(BaseOperation):
    op: Literal["actualityGroupBy"]

    def apply(self, df: DataFrame) -> DataFrame:
        columns = df.columns
        columns = [
            column
            for column in columns
            if column
            not in {ColumnTypes.ACTUALITY.value, ColumnTypes.SOURCE_ENTITY_ID.value}
        ]
        return (
            df.groupBy(columns)
            .agg(
                max(
                    struct(
                        ColumnTypes.ACTUALITY.value, ColumnTypes.SOURCE_ENTITY_ID.value
                    )
                ).alias(TempColumnNames.MAX_STRUCT.value)
            )
            .select("*", f"{TempColumnNames.MAX_STRUCT.value}.*")
            .drop(TempColumnNames.MAX_STRUCT.value)
        )
