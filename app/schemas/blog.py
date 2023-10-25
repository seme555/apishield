from pydantic import BaseModel, UUID4
from typing import Optional

from app.schemas.base import AppBaseModel


class BlogBasic(BaseModel):
    title: str
    sub_title: str = None
    author: UUID4


class BlogBasicWithAuthor(BlogBasic):
    author: UUID4


class BlogId(BaseModel):
    id: UUID4
