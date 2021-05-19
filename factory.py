import motor
from beanie import init_beanie
from fastapi import FastAPI
from pydantic import BaseSettings

from news.models import Category, Post, Tag
from news.routes import categories_router, posts_router, tags_router

app = FastAPI()


class Settings(BaseSettings):
    mongo_host: str = "localhost"
    mongo_user: str = "beanie"
    mongo_pass: str = "beanie"
    mongo_db: str = "beanie_db"

    @property
    def mongo_dsn(self):
        return f"mongodb://{self.mongo_user}:{self.mongo_pass}@{self.mongo_host}:27017/{self.mongo_db}"


@app.on_event("startup")
async def app_init():
    # CREATE MOTOR CLIENT
    client = motor.motor_asyncio.AsyncIOMotorClient(
        Settings().mongo_dsn
    )

    # INIT BEANIE
    await init_beanie(client.beanie_db, document_models=[Category, Post, Tag])

    # ADD ROUTES
    app.include_router(categories_router, prefix="/v1", tags=["categories", "posts"])
    app.include_router(posts_router, prefix="/v1", tags=["posts"])
    app.include_router(tags_router, prefix="/v1", tags=["tags"])
