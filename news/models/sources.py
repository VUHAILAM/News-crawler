from typing import Optional, List
from pydantic import BaseModel
from .base import RootModel


class SourceInput(BaseModel):
    url: str
    language: str
    config: str
    schedule: Optional[List[str]] = []


class Source(SourceInput, RootModel):
    pass
