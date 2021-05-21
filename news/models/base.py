from datetime import datetime

from beanie import Document


class RootModel(Document):
    created_at: datetime = None
