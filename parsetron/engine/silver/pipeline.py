import logging

from pyspark.sql import SparkSession

from parsetron.engine.silver.config import Silver
from parsetron.engine.silver.ingest import Ingest
from parsetron.engine.utils.splitter import split_by
from parsetron.engine.utils.track import track_execution_time

logger = logging.getLogger(__name__)


@track_execution_time(logger, "SILVER Stage")
def run_silver(
    spark_session: SparkSession,
    configs: list[Silver],
    bronze_path: str,
    out_path: str,
    group_ids: str,
    entities: str,
):
    parsed_group_ids = split_by(group_ids)
    parsed_entities = split_by(entities)
    Ingest(
        spark_session, configs, parsed_group_ids, parsed_entities, bronze_path, out_path
    ).run()
