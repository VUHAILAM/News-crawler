from typing import Optional, List

from beanie import Document


class Post(Document):
    title: str
    content: str
    url: str
    categories: Optional[List[str]] = []
    tags: Optional[List[str]] = []
    raw_html: str
