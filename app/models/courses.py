from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator 

from .base import BaseModel
import models 



class Course(BaseModel):
    title = fields.CharField(max_length=200, required=True, unique=True)
    description = fields.TextField(required=True)
    price = fields.FloatField(required=True)
    author = fields.ForeignKeyField("models.User", related_name="courses")

    def __str__(self):
        return self.title


CoursePydantic = pydantic_model_creator(
    Course,
    name="Course",
    include=(
        "id",
        "title",
        "description",
        "price",
        "author",
    )
)

CourseInPydantic = pydantic_model_creator(
    Course,
    name="CourseIn",
    include=(
        "title",
        "description",
        "price",
        "author",
    ),
    exclude_readonly=True
)