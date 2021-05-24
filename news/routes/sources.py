from typing import List

from fastapi import APIRouter, HTTPException, Depends, status

from news.models.source import Source

sources_router = APIRouter()


async def get_source(source_id: PydanticObjectId) -> Source:
    source = await Source.get(source_id)
    if source is None:
        raise HTTPException(status_code=404, detail="Source not found")
    return source


@sources_router.post("/sources", response_model=Source, status_code=status.HTTP_201_CREATED)
async def create_source(source_input: Source):
    source = Source(**source_input.dict())
    await source.create()
    return source


@sources_router.get("/sources/{source_id}", response_model=Source)
async def get_source(source: Source = Depends(get_source)):
    return source


@sources_router.delete("/sources/{source_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(source: Source = Depends(get_source)):
    await source.delete()
    return source


# LISTS

@sources_router.get("/sources", response_model=List[Source])
async def get_all_posts():
    return await Source.find_all().to_list()
