from typing import Optional, List

from beanie import Document

from .categories import Category
from .tags import Tag


class Post(Document):
    title: str
    content: str
    url: str
    categories: Optional[List[Category]] = []
    tags: Optional[List[Tag]] = []
    raw_html: str
