import logging
from functools import reduce

from pyspark.sql import SparkSession

from parsetron.engine.constants import StageTypes, ColumnTypes, JoinTypes
from parsetron.engine.silver.config import Silver, SilverEntity
from parsetron.engine.silver.processor import Processor
from parsetron.engine.silver.reader import Reader
from parsetron.engine.silver.writer import Writer
from parsetron.engine.utils.generator.date import get_current_iso_date
from parsetron.engine.utils.path import rename_ingest_date_dir
from parsetron.engine.utils.track import track_execution_entity_time

logger = logging.getLogger(__name__)


class Ingest:
    stage: str = StageTypes.SILVER.name

    def __init__(
        self,
        spark: SparkSession,
        configs: list[Silver],
        group_ids: list[str],
        entities: list[str],
        in_path: str,
        out_path: str,
    ):
        self.configs = configs
        self.group_ids = group_ids
        self.entities = entities
        self.out_path = out_path

        self.ingest_date = get_current_iso_date()
        self.reader = Reader(spark, in_path)
        self.processor = Processor()
        self.writer = Writer(out_path, self.ingest_date)

    def run(self) -> None:
        if not self.configs:
            logger.warning(f"There is nothing to process for {self.stage}")
            return
        self._process()

    def _process(self) -> None:
        rename_ingest_date_dir(logger, self.out_path, self.ingest_date)

        for config in self.configs:
            if config.id and self.group_ids and config.id not in self.group_ids:
                logger.info(f"{config.id} is skipping")
                continue
            for entity in config.entities.keys():
                if self.entities and entity not in self.entities:
                    continue
                func = lambda: self._process_entity(
                    config.entities[entity], config.id, entity
                )
                track_execution_entity_time(logger, self.stage, entity, func)

    def _process_entity(self, config: SilverEntity, group_id: str, entity: str) -> None:
        if config.entities:
            df = reduce(
                lambda left, right: left.join(
                    right,
                    on=ColumnTypes.SOURCE_ENTITY_ID.value,
                    how=JoinTypes.OUTER.value,
                ),
                [
                    self.reader.read(group_id, entity_name)
                    for entity_name in config.entities
                ],
            )
        else:
            df = self.reader.read(group_id, entity)
        processed_df = self.processor.process(df, config.columns)
        self.writer.write(processed_df, group_id, entity, config=config.io.write)
