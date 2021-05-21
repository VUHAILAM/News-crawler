from datetime import datetime
from typing import Optional, List

import pymongo
from beanie import Document


class Post(Document):
    title: str
    content: str
    source: Optional[str] = ""
    url: str
    categories: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    raw_html: str
    published_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

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
