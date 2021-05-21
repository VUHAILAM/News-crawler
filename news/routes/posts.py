from datetime import datetime
from typing import List

from beanie import PydanticObjectId
from beanie.operators import Text
from fastapi import APIRouter, HTTPException, Depends, status

from news.models import Post
from news.models.posts import PostInput

posts_router = APIRouter()


async def get_post(post_id: PydanticObjectId) -> Post:
    post = await Post.get(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


# CRUD


@posts_router.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post_input: PostInput):
    post = Post(**post_input.dict())
    post.created_at = datetime.utcnow()
    await post.create()
    return post


@posts_router.get("/posts/{post_id}", response_model=Post)
async def get_post(post: Post = Depends(get_post)):
    return post


@posts_router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post: Post = Depends(get_post)):
    await post.delete()
    return post


# LISTS

@posts_router.get("/posts", response_model=List[Post])
async def get_all_posts(limit: int = 10, skip: int = 0, search: str = None):
    query = []
    if search:
        query.append(Text(search=search))
    return await Post.find(*query).sort(-Post.id).limit(limit).skip(skip).to_list()
