from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator 

from .base import BaseModel


class User(BaseModel):
    email = fields.CharField(max_length=200, required=True, unique=True)
    password = fields.CharField(max_length=200, required=True)
    username = fields.CharField(max_length=200, required=True)
    is_admin = fields.BooleanField(default=False)

    def __str__(self):
        return self.username



UserPydantic = pydantic_model_creator(
    User,
    name="User",
    include=(
        "id",
        "email",
        "username",
    )
)


UserInPydantic = pydantic_model_creator(
    User,
    name="UserIn",
    include=(
        "email",
        "password",
        "username",
    ),
    exclude_readonly=True
)