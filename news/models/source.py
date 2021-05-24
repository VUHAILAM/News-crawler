from beanie import Document
from typing import Optional, List, Dict
from pydantic import Json, BaseModel
from .base import RootModel


class SourceInput(BaseModel):
    url: str
    language: str
    config: str
    schedule: Optional[List[str]] = []


class Source(SourceInput, RootModel):
    pass

