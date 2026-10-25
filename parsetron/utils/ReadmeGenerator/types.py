from typing import TypedDict, Optional


class ReadmeDataset(TypedDict):
    code_name: Optional[str]
    path: Optional[str]
    total: int
    schema: str
    data_sample: str
