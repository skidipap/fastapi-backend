from fastapi import APIRouter, HTTPException
from typing import List 
from uuid import UUID 

import models 


tags = ["Course"]
router = APIRouter(
    prefix="/course",
    tags=tags
)


@router.post("/{user_id}", response_model=models.CoursePydantic)
async def create_course(user_id: UUID, data: models.CourseInPydantic):
    user = await models.User.get(id=user_id)
    course_obj = await models.Course.create(**data.dict(exclude_unset=True), author=user)

    return await models.CoursePydantic.from_tortoise_orm(course_obj)


# @router.get("/{course_id}")