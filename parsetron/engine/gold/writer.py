import logging
from pathlib import Path
from typing import Optional

from pyspark import StorageLevel
from pyspark.sql import DataFrame

from parsetron.engine.gold.config import IOParams
from parsetron.engine.md import OutMdData
from parsetron.engine.utils.repartition import repartition

logger = logging.getLogger(__name__)


class GoldWriter:
    def __init__(
        self,
        gold_root: str,
        ingest_date: str,
        md_processor: Optional[OutMdData],
        config: Optional[IOParams] = None,
    ):
        self.gold_root = Path(gold_root)
        self.ingest_date = ingest_date
        self.md_processor = md_processor
        self.config = config

    def write(
        self,
        df: DataFrame,
        mode: str = "overwrite",
        compression: str = "gzip",
        date_format: str = "dd.MM.yyyy",
    ) -> None:
        path = self._prepare_path()
        df.persist(StorageLevel.DISK_ONLY)
        if self.md_processor:
            self.md_processor.find_stat_out(df, path)
        repartition(logger, df, self.config).write.json(
            path=path, mode=mode, compression=compression, dateFormat=date_format
        )
        logger.info(f"path: {path}\n%s", df.schema.treeString())

    def _prepare_path(self) -> str:
        target_path = self.gold_root / f"ingest_date={self.ingest_date}" / "upload"
        target_path.parent.mkdir(parents=True, exist_ok=True)
        return str(target_path)
