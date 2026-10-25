import logging
from typing import Optional

from pyspark.sql import DataFrame, SparkSession

from parsetron.engine.bronze.config import Bronze, BronzeEntity
from parsetron.engine.bronze.helpers.preprocessor import (
    preprocess,
    validate_no_id_collisions,
)
from parsetron.engine.bronze.processor import Processor
from parsetron.engine.bronze.reader import OnlyReader
from parsetron.engine.bronze.reader import Reader
from parsetron.engine.bronze.writer import Writer
from parsetron.engine.constants import StageTypes
from parsetron.engine.md import InMdData
from parsetron.engine.utils.generator.date import get_current_iso_date
from parsetron.engine.utils.path import rename_ingest_date_dir
from parsetron.engine.utils.track import track_execution_entity_time

logger = logging.getLogger(__name__)


class Ingest:
    stage: str = StageTypes.BRONZE.name

    def __init__(
        self,
        spark: SparkSession,
        source_entity_id_type: str,
        configs: list[Bronze],
        out_path: str,
        group_ids: list[str],
        entities: list[str],
        md_processor: Optional[InMdData],
        read_only: bool = False,
        limit: Optional[int] = None,
    ):
        self.configs = configs
        self.read_only = read_only

        if not self.read_only:
            self.out_path = out_path
            self.group_ids = group_ids
            self.entities = entities
            self.source_entity_id_type = source_entity_id_type
            self.ingest_date = get_current_iso_date()
            self.reader = Reader(spark, md_processor, limit)
            self.processor = Processor()
            self.writer = Writer(self.out_path, self.ingest_date)
        else:
            self.reader = OnlyReader(spark, md_processor, limit)

    def run(self) -> None:
        if not self.configs:
            logger.warning(f"No configurations provided for stage: {self.stage}")
            return
        self._process()

    def _process(self) -> None:
        if self.read_only:
            logger.info("Running BRONZE in READ-ONLY mode")
            for config in self.configs:
                self.reader.read(config.read)
            return

        rename_ingest_date_dir(logger, self.out_path, self.ingest_date)
        datasets: dict[str, tuple[Bronze, DataFrame]] = {}

        for config in self.configs:
            if config.id and self.group_ids and config.id not in self.group_ids:
                logger.info(f"Skipping {config.id}: Not in group IDs")
                continue

            if config.id:
                logger.info(f"Starting ingestion for entity: {config.id}")
            raw_df = self.reader.read(config.read)
            processed_df = preprocess(raw_df, self.source_entity_id_type, config)
            datasets[config.id] = (config, processed_df)

        if len(datasets) > 1:
            dfs = [df for _, df in datasets.values()]
            validate_no_id_collisions(dfs)

        for _, (config, df) in datasets.items():
            self._process_entities(config, df)
            if config.after_read.cache:
                logger.info(f"Unpersisting DataFrame for {config.read.path}")
                df.unpersist()

    def _process_entities(self, config: Bronze, df: DataFrame) -> None:
        for entity, e_config in config.entities.items():
            if self.entities and entity not in self.entities:
                continue
            func = lambda: self._process_entity(df, e_config, config.id, entity)
            track_execution_entity_time(logger, self.stage, entity, func)

    def _process_entity(
        self, df: DataFrame, config: BronzeEntity, group_id: str, entity: str
    ) -> None:
        processed_df = self.processor.process(df, config.columns)
        self.writer.write(processed_df, group_id, entity, config=config.io.write)
