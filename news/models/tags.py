from typing import Optional

from pydantic import BaseModel

from .base import RootModel


class TagInput(BaseModel):
    name: str
    description: Optional[str] = ""


class Tag(TagInput, RootModel):
    pass
