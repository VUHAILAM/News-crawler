from datetime import datetime
from typing import Optional, List

import pymongo
from pydantic import BaseModel
from .base import RootModel


class PostInput(BaseModel):
    title: str
    content: str
    source: str = None
    url: str
    categories: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    raw_html: Optional[str] = None
    published_at: Optional[datetime] = None


class Post(PostInput, RootModel):
    class Collection:
        indexes = [
            [
                ("title", pymongo.TEXT),
                ("content", pymongo.TEXT),
                ("source", pymongo.TEXT),
                ("categories", pymongo.TEXT),
                ("tags", pymongo.TEXT),
            ]
        ]
