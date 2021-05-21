from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, Depends, status

from news.models import Category

categories_router = APIRouter()


async def get_category(category_id: PydanticObjectId) -> Category:
    category = await Category.get(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


# CRUD


@categories_router.post("/categories", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(category: Category):
    await category.create()
    return category


@categories_router.get("/categories/{category_id}", response_model=Category)
async def get_category(category: Category = Depends(get_category)):
    return category


@categories_router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category: Category = Depends(get_category)):
    await category.delete()
    return category


# LISTS


@categories_router.get("/categories", response_model=List[Category])
async def get_all_categories():
    return await Category.find_all().to_list()
