from typing import Optional

from parsetron.engine.bronze.readers.base import BaseReader
from parsetron.engine.bronze.readers.csv import CsvReader
from parsetron.engine.md import InMdData


class ReaderFactory:
    READERS = {
        "csv": CsvReader,
    }

    @classmethod
    def create(cls, spark, fmt: str, md_processor: Optional[InMdData], limit: Optional[int] = None) -> BaseReader:
        if fmt not in cls.READERS:
            raise ValueError(f"Unsupported input format: {fmt}")
        return cls.READERS[fmt](spark, md_processor, limit)
