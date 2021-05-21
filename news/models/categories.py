from typing import Optional

from pydantic import BaseModel

from .base import RootModel


class CategoryInput(BaseModel):
    name: str
    description: Optional[str] = ""


class Category(CategoryInput, RootModel):
    pass
