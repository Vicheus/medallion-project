import logging
from typing import Optional

from pyspark.sql import SparkSession

from parsetron.engine.gold.config import Gold
from parsetron.engine.gold.ingest import Ingest
from parsetron.engine.md import OutMdData
from parsetron.engine.utils.track import track_execution_time

logger = logging.getLogger(__name__)


@track_execution_time(logger, "GOLD Stage")
def run_gold(
    spark_session: SparkSession,
    config: Gold,
    source_entity_id_hash_type: str,
    bronze_path: str,
    in_path: str,
    out_path: str,
    md_processor: Optional[OutMdData] = None,
):
    Ingest(
        spark_session,
        config,
        source_entity_id_hash_type,
        bronze_path,
        in_path,
        out_path,
        md_processor,
    ).run()
