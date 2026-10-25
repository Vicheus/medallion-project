import logging
from typing import Optional

from pyspark.sql import DataFrame

from parsetron.engine.config.common import IOParams
from parsetron.engine.utils.repartition import repartition

logger = logging.getLogger(__name__)


class Writer:
    def __init__(self, out_path: str, ingest_date: str):
        self.out_path = out_path
        self.ingest_date = ingest_date

    def write(
        self,
        df: DataFrame,
        group_id: str,
        entity: str,
        mode: str = "overwrite",
        config: Optional[IOParams] = None,
    ) -> None:
        path = self._create_path(entity, group_id)
        logger.info(f"path: {path}\n%s", df.schema.treeString())
        repartition(logger, df, config).write.mode(mode).parquet(path)

    def _create_path(self, entity: str, group_id: str) -> str:
        if group_id:
            g_id = f"group_id={group_id}/"
            return f"{self.out_path}/ingest_date={self.ingest_date}/{g_id}{entity}"
        return f"{self.out_path}/ingest_date={self.ingest_date}/{entity}"
