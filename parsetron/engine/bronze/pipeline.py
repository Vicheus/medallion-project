import logging
from typing import Optional

from pyspark.sql import SparkSession

from parsetron.engine.bronze.config import Bronze
from parsetron.engine.bronze.ingest import Ingest
from parsetron.engine.md import InMdData
from parsetron.engine.utils.splitter import split_by
from parsetron.engine.utils.track import track_execution_time

logger = logging.getLogger(__name__)


@track_execution_time(logger, "BRONZE Stage")
def run_bronze(
    spark_session: SparkSession,
    source_entity_id_type: str,
    configs: list[Bronze],
    out_path: str,
    group_ids: str,
    entities: str,
    md_processor: Optional[InMdData] = None,
    read_only: bool = False,
    limit: Optional[int] = None,
):
    parsed_group_ids = split_by(group_ids)
    parsed_entities = split_by(entities)
    Ingest(
        spark_session,
        source_entity_id_type,
        configs,
        out_path,
        parsed_group_ids,
        parsed_entities,
        md_processor,
        read_only,
        limit,
    ).run()
