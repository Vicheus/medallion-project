import logging
from typing import Optional

from pyspark.sql import SparkSession

from parsetron.engine.constants import StageTypes
from parsetron.engine.gold.config import Gold
from parsetron.engine.gold.processor import GoldProcessor
from parsetron.engine.gold.reader import Reader
from parsetron.engine.gold.writer import GoldWriter
from parsetron.engine.md import OutMdData
from parsetron.engine.utils.generator.date import get_current_iso_date

logger = logging.getLogger(__name__)


class Ingest:
    stage: str = StageTypes.GOLD.name

    def __init__(
        self,
        spark: SparkSession,
        config: Gold,
        source_entity_id_hash_type: str,
        bronze_path: str,
        in_path: str,
        out_path: str,
        md_processor: Optional[OutMdData],
    ):
        self.ids = config.ids
        self.ingest_date = get_current_iso_date()
        self.bronze_path = bronze_path
        self.silver_path = in_path

        self.reader = Reader(spark)
        self.processor = GoldProcessor(
            source_entity_id_hash_type, bronze_path=bronze_path, config=config
        )
        self.writer = GoldWriter(
            out_path, self.ingest_date, md_processor, config=config.io.write
        )

    def run(self):
        if self.ids:
            dfs = self.reader.read_all_groups(self.silver_path)
            read_bronze_dfs = lambda: [
                df
                for inner in self.reader.read_all_groups(self.bronze_path).values()
                for df in inner.values()
            ]
            df_gold = self.processor.process_group(dfs, read_bronze_dfs)
        else:
            dfs = self.reader.read_all(self.silver_path)
            read_bronze_dfs = lambda: list(
                self.reader.read_all(self.bronze_path).values()
            )
            df_gold = self.processor.process(dfs, read_bronze_dfs)
        self.writer.write(df_gold)
