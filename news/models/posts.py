from typing import Optional, List

import pymongo
from beanie import Document


class Post(Document):
    title: str
    content: str
    url: str
    categories: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    raw_html: str

    class Collection:
        indexes = [
            [("title", pymongo.TEXT), ("content", pymongo.TEXT)],
        ]
