from fastapi import APIRouter, HTTPException
from typing import List 
from uuid import UUID 

import models 


tags = ["User"]
router = APIRouter(
    prefix="/user",
    tags=tags
)


@router.post("/", response_model=models.UserPydantic)
async def create_user(data: models.UserInPydantic):
    new_user = await models.User.create(**data.dict(exclude_unset=True))
    
    return await models.UserPydantic.from_tortoise_orm(new_user)


@router.get("/", response_model=List[models.UserPydantic])
async def get_all_users():
    user_obj = models.User.all()

    return await models.UserPydantic.from_queryset(user_obj)


@router.get("/{user_id}", response_model=models.UserPydantic)
async def get_user_by_id(user_id: UUID):
    user_obj = await models.User.filter(id=user_id).first()

    return await models.UserPydantic.from_tortoise_orm(user_obj)


@router.put("/{user_id}", response_model=models.UserPydantic)
async def change_info(user_id: UUID, data: models.UserInPydantic):
    user_obj = await models.User.filter(
        id=user_id).update(**data.dict(exclude_unset=True)
        )
    user_obj = await models.User.filter(id=user_id).first()

    return await models.UserPydantic.from_tortoise_orm(user_obj)


@router.delete("/{user_id}")
async def delete_user(user_id: UUID):
    user_obj = await models.User.filter(id=user_id).delete()

    if not user_obj:
        raise HTTPException(status_code=404, detail=f"User Not Found")
    
    return {
        "detail" : "succes",
        "data" : f"User {user_id} deleted"
    }