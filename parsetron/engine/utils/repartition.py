import logging
from logging import Logger
from math import ceil
from typing import Optional

from pyspark.sql import DataFrame

from parsetron.engine.config.common import IOParams


def repartition(
    logger: logging.Logger, df: DataFrame, config: Optional[IOParams]
) -> DataFrame:
    if not config:
        return df
    if config.type == "repartition":
        partitions = _find_partition(config, df, config.type, logger)
        return df.repartition(partitions)
    if config.type == "coalesce":
        partitions = _find_partition(config, df, config.type, logger)
        return df.coalesce(partitions)

    return df.coalesce(
        _find_optimal_partition(logger, df, config.count)
        if config.count
        else _find_optimal_partition(logger, df)
    )


def _find_partition(
    config: IOParams, df: DataFrame, partition_type: str, logger: Logger
) -> int:
    current_partitions = df.rdd.getNumPartitions()
    partitions = min(current_partitions, config.count)
    if partitions != current_partitions:
        logger.info(
            f"Will {partition_type} from {current_partitions} to {partitions} partitions"
        )
    return partitions


def _find_optimal_partition(
    logger: logging.Logger, df: DataFrame, desired_size: int = 512
) -> int:
    dataset = df.rdd
    partitions = dataset.getNumPartitions()
    total_data_size = float(dataset.map(lambda r: len(str(r))).sum()) / (1024 * 1024)
    new_partitions = max(1, ceil(total_data_size / desired_size))
    if partitions == new_partitions:
        logger.info(f"Will coalesce from {partitions} to {new_partitions} partitions")
    return new_partitions
