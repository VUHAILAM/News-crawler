from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Depends

from news.models import Post

posts_router = APIRouter()


async def get_post(post_id: PydanticObjectId) -> Post:
    post = await Post.get(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


# CRUD


@posts_router.get("/posts/{post_id}", response_model=Post)
async def get_post(post: Post = Depends(get_post)):
    return post


@posts_router.post("/posts", response_model=Post, status_code=201)
async def create_post(post: Post):
    await post.create()
    return post


@posts_router.delete("/posts/{post_id}", status_code=204)
async def delete_post(post: Post = Depends(get_post)):
    await post.delete()
    return post


# LISTS


@posts_router.get("/posts", response_model=List[Post])
async def get_all_posts():
    return await Post.find_all().to_list()
