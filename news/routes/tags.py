from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Depends, status

from news.models import Tag

tags_router = APIRouter()


async def get_tag(tag_id: PydanticObjectId) -> Tag:
    tag = await Tag.get(tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


# CRUD


@tags_router.post("/tags", response_model=Tag, status_code=status.HTTP_201_CREATED)
async def create_tag(tag: Tag):
    await tag.create()
    return tag


@tags_router.get("/tags/{tag_id}", response_model=Tag)
async def get_tag(tag: Tag = Depends(get_tag)):
    return tag


@tags_router.delete("/tags/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tag(tag: Tag = Depends(get_tag)):
    await tag.delete()
    return tag


# LISTS


@tags_router.get("/tags", response_model=List[Tag])
async def get_all_tags():
    return await Tag.find_all().to_list()
