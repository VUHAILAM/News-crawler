from typing import Optional

from beanie import Document


class Category(Document):
    name: str
    description: Optional[str] = ""
