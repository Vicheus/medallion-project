import logging
from functools import reduce
from operator import or_
from typing import Optional, Callable

from pyspark import StorageLevel
from pyspark.sql import DataFrame, Column
from pyspark.sql.functions import (
    array_sort,
    col,
    collect_set,
    element_at,
    first,
    lit,
    max,
    raise_error,
    size,
    when,
)

from parsetron.engine.constants import (
    EntityTypes,
    JoinTypes,
    ColumnTypes,
    ColumnAggTypes,
    SourceIdTypes,
    TempColumnNames,
    StageTypes,
)
from parsetron.engine.gold.config import Gold
from parsetron.engine.registry.functions.base import BaseAction
from parsetron.engine.registry.transformations.base import BaseOperation
from parsetron.engine.utils.generator.id import (
    hash_xxhash64,
    hash_sha224,
    concat_values,
)
from parsetron.engine.utils.hash import check_hash_collisions

logger = logging.getLogger(__name__)

HASH_FUNC_MAP = {
    SourceIdTypes.NUM_HASH_ID.value: hash_xxhash64,
    "DEFAULT": hash_sha224,
}


def _sort_col_names(columns: list[str]):
    allowed_columns = [column.value for column in ColumnTypes]
    allowed_columns_ordered = {s: i for i, s in enumerate(allowed_columns)}

    in_columns = [x for x in columns if x in allowed_columns_ordered]
    out_columns = [x for x in columns if x not in allowed_columns_ordered]

    sorted_in_ref = sorted(in_columns, key=lambda x: allowed_columns_ordered[x])
    sorted_not_in_ref = sorted(out_columns)

    return sorted_in_ref + sorted_not_in_ref


def _join(datasets: dict[str, DataFrame]) -> DataFrame:
    df = datasets[EntityTypes.PERSONS.value]
    other_dfs = (v for k, v in datasets.items() if k != EntityTypes.PERSONS.value)
    for other_df in other_dfs:
        df = df.join(
            other_df, on=ColumnTypes.SOURCE_ENTITY_ID.value, how=JoinTypes.LEFT.value
        )
    return df


def _define_simple_agg_col(column: str) -> Optional[Column]:
    if column in ColumnAggTypes.MAX.value:
        return max(col(column)).alias(column)
    if (
        column in ColumnAggTypes.ANY.value
        or column in ColumnAggTypes.GENERATED_ID.value
    ):
        return (
            when(
                size(collect_set(col(column))) > 1,
                raise_error(lit(f"Multiple values found for {column}")),
            )
            .otherwise(first(col(column), ignorenulls=True))
            .alias(column)
        )

    return None


def _define_agg_col(column: str) -> Column:
    expr = _define_simple_agg_col(column)
    if expr is not None:
        return expr
    return array_sort(collect_set(col(column))).alias(column)


def _group_together(df: DataFrame) -> DataFrame:
    agg_cols = (
        _define_agg_col(column)
        for column in df.columns
        if column != ColumnTypes.SOURCE_ENTITY_ID.value
    )
    return df.groupBy(ColumnTypes.SOURCE_ENTITY_ID.value).agg(*agg_cols)


def _nullify(df: DataFrame, columns: list[str]) -> DataFrame:
    for column in columns:
        if column not in ColumnAggTypes.SCALARS.value:
            df = df.withColumn(column, when(size(col(column)) > 0, col(column)))
    return df


def _apply_operations(df: DataFrame, transformations: list[BaseOperation]) -> DataFrame:
    for transform in transformations:
        df = transform.apply(df)
    return df


def _preprocess(
    datasets: dict[str, DataFrame], transformations: list[BaseOperation]
) -> DataFrame:
    df = _join(datasets)
    df = _group_together(df)
    return _apply_operations(df, transformations)


class GoldProcessor:
    def __init__(self, source_entity_id_hash_type: str, bronze_path: str, config: Gold):
        self.source_entity_id_hash_type = source_entity_id_hash_type
        self.bronze_path = bronze_path
        self.config = config

    def process(
        self, datasets: dict[str, DataFrame], read_ids: Callable[[], list[DataFrame]]
    ) -> DataFrame:
        df = _preprocess(datasets, self.config.transformations)
        return self._finalize(df, read_ids)

    def process_group(
        self,
        datasets: dict[str, dict[str, DataFrame]],
        read_ids: Callable[[], list[DataFrame]],
    ) -> DataFrame:
        joined_datasets = []
        for group in self.config.ids:
            df = _preprocess(datasets[group.id], group.transformations)
            joined_datasets.append(df)
        df = reduce(
            lambda df1, df2: df1.unionByName(df2, allowMissingColumns=True),
            joined_datasets,
        )
        df = _apply_operations(df, self.config.transformations)
        return self._finalize(df, read_ids)

    def _finalize(
        self, df: DataFrame, read_ids: Callable[[], list[DataFrame]]
    ) -> DataFrame:
        columns = df.columns
        df = _nullify(df, columns)
        result_columns = _sort_col_names(columns)
        df = df.select(*result_columns)
        df = self._filter(df)
        df = self._process_hashes(df, read_ids)
        check_hash_collisions(df, self.config.ignore_hash_error)
        return df

    def _filter(self, df: DataFrame) -> DataFrame:
        if isinstance(self.config.remain, BaseAction):
            expr = self.config.remain.apply()
        else:
            conditions = (col(column).isNotNull() for column in self.config.remain)
            expr = col(ColumnTypes.NAMES.value).isNotNull() & reduce(or_, conditions)
        return df.filter(expr)

    def _process_hashes(
        self, df: DataFrame, read_ids: Callable[[], list[DataFrame]]
    ) -> DataFrame:
        source_entity_id_type = [
            col_type
            for col_name, col_type in df.dtypes
            if col_name == ColumnTypes.SOURCE_ENTITY_ID.value
        ][0]
        if source_entity_id_type != "array<string>":
            return df

        if self.source_entity_id_hash_type in {
            SourceIdTypes.INCREASING_ID.value,
            SourceIdTypes.SORTED_INCREASING_ID.value,
        }:
            logger.info(
                f"Max value of {ColumnTypes.SOURCE_ENTITY_ID.value} will be selected due to {self.source_entity_id_hash_type} ID type"
            )
            return df.withColumn(
                ColumnTypes.SOURCE_ENTITY_ID.value,
                max(ColumnTypes.SOURCE_ENTITY_ID.value),
            )
        logger.info(
            f"New hashes will be constructed based on multiple values due to {self.source_entity_id_hash_type} ID type"
        )
        hash_func = HASH_FUNC_MAP.get(
            self.source_entity_id_hash_type, HASH_FUNC_MAP["DEFAULT"]
        )

        df = (
            df.withColumn(
                TempColumnNames.SOURCE_ENTITY_ID.value,
                col(ColumnTypes.SOURCE_ENTITY_ID.value),
            )
            .withColumn(
                ColumnTypes.SOURCE_ENTITY_ID.value,
                when(
                    size(col(ColumnTypes.SOURCE_ENTITY_ID.value)) > 1,
                    hash_func(concat_values(col(ColumnTypes.SOURCE_ENTITY_ID.value))),
                ).otherwise(element_at(col(ColumnTypes.SOURCE_ENTITY_ID.value), 1)),
            )
            .persist(StorageLevel.DISK_ONLY)
        )
        initial_dfs = read_ids()
        collision_df = (
            reduce(
                lambda df1, df2: df1.union(df2),
                [
                    initial_df.select(ColumnTypes.SOURCE_ENTITY_ID.value)
                    for initial_df in initial_dfs
                ],
            )
            .distinct()
            .join(
                df.filter(size(col(TempColumnNames.SOURCE_ENTITY_ID.value)) > 1).select(
                    ColumnTypes.SOURCE_ENTITY_ID.value
                ),
                ColumnTypes.SOURCE_ENTITY_ID.value,
            )
        )
        if not collision_df.isEmpty():
            raise ValueError(
                f"Newly generated hash collision with {StageTypes.BRONZE} detected: {collision_df.count()}"
            )
        return df.drop(col(TempColumnNames.SOURCE_ENTITY_ID.value))
