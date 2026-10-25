import logging
from functools import reduce

from pyspark import StorageLevel
from pyspark.sql import DataFrame, Window
from pyspark.sql.functions import struct, collect_set, col, size

from parsetron.engine.bronze.config import Bronze, BronzeEntity
from parsetron.engine.constants import SourceIdTypes, ColumnTypes
from parsetron.engine.utils.generator.id import (
    add_row_number_id,
    add_xxhash64_id,
    add_sha224_id,
    add_monotonically_increasing_id,
)

logger = logging.getLogger(__name__)


def _add_source_entity_id(df: DataFrame, source_entity_id: str) -> DataFrame:
    id_functions = {
        SourceIdTypes.SORTED_INCREASING_ID.value: add_row_number_id,
        SourceIdTypes.NUM_HASH_ID.value: add_xxhash64_id,
        SourceIdTypes.INCREASING_ID.value: add_monotonically_increasing_id,
    }

    func = id_functions.get(source_entity_id, add_sha224_id)
    logger.info(
        f"Applying ID generation strategy: `{source_entity_id or SourceIdTypes.SHA_HASH_ID.value}`"
    )
    return func(df)


def _get_collision_rows(df: DataFrame):
    data_columns = [c for c in df.columns if c != ColumnTypes.SOURCE_ENTITY_ID.value]
    window_spec = Window.partitionBy(*data_columns)
    df.withColumn(
        "_unique_records_per_id",
        size(collect_set(struct([ColumnTypes.SOURCE_ENTITY_ID.value])).over(window_spec)),
    ).filter(col("_unique_records_per_id") > 1).drop("_unique_records_per_id").show(
        10, False
    )


def _check_hash_collisions(df: DataFrame):
    ids = df.select(ColumnTypes.SOURCE_ENTITY_ID.value).distinct().count()
    records = df.drop(ColumnTypes.SOURCE_ENTITY_ID.value).distinct().count()
    if ids != records:
        error_msg = f"Hash ID collision occurred: {ids} hashes, {records} records"
        logger.error(error_msg)
        raise ValueError(error_msg)


def _find_required_cols(entities: dict[str, BronzeEntity]) -> list[str]:
    required_columns: set[str] = set()
    for entity in entities.values():
        for column in entity.columns.values():
            required_columns.add(column if isinstance(column, str) else column.source)
    return list(required_columns)


def preprocess(df: DataFrame, source_entity_id_type: str, config: Bronze) -> DataFrame:
    required_cols = sorted(_find_required_cols(config.entities))
    df = df.select(*required_cols)

    if config.after_read.distinct:
        logger.info(f"Performing distinct on {config.read.path}")
        df = df.distinct()

    df = _add_source_entity_id(df, source_entity_id_type)
    if config.after_read.cache:
        logger.info(f"Persisting DataFrame for {config.read.path}")
        df = df.persist(StorageLevel.DISK_ONLY)
    _check_hash_collisions(df)
    return df


def validate_no_id_collisions(df_list: list[DataFrame]):
    if not df_list:
        return

    logger.info("Starting cross-dataset collision validation")
    combined_df = reduce(lambda df1, df2: df1.unionByName(df2, True), df_list)
    _check_hash_collisions(combined_df)
    logger.info("Cross-dataset collision validation passed")
