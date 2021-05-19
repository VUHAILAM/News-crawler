from typing import List, Optional

from beanie import Document


class Category(Document):
    name: str
    description: str


class Tag(Document):
    name: str
    description: str


class Post(Document):
    title: str
    content: str
    url: str
    categories: Optional[List[Category]] = []
    tags: Optional[List[Tag]] = []
    raw_html: str
