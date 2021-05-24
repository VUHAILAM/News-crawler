import os

from beanie import init_beanie
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from motor import motor_asyncio
from pydantic import BaseSettings

from middlewares import apply_cors
from news.models import Category, Post, Tag, Source
from news.routes import categories_router, posts_router, tags_router, sources_router

app = FastAPI()

app.mount("/admin", StaticFiles(directory="admin/dist", html=True), name="admin")

apply_cors(app)


class Settings(BaseSettings):
    @property
    def mongo_dsn(self):
        return os.getenv("MONGO_DSN", "mongodb://beanie:beanie@localhost:27017/beanie_db")


@app.on_event("startup")
async def app_init():
    # CREATE MOTOR CLIENT
    client = motor_asyncio.AsyncIOMotorClient(
        Settings().mongo_dsn
    )

    # INIT BEANIE
    await init_beanie(client.beanie_db, document_models=[Category, Post, Tag, Source])

    # ADD ROUTES
    app.include_router(categories_router, prefix="/v1", tags=["categories"])
    app.include_router(posts_router, prefix="/v1", tags=["posts"])
    app.include_router(tags_router, prefix="/v1", tags=["tags"])
