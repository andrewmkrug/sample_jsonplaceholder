from typing import List

import pydantic.class_validators
from pydantic import BaseModel, EmailStr, validator

# Some more validators can be written if we know that all IDs are supposed to be postive numbers.

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str
    
    @validator('*', each_item=True, allow_reuse=True)
    def check_values_not_empty(cls, v):
        assert v != '', 'Empty strings are not allowed.'
        return v

class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: EmailStr
    body: str

    @validator('*', each_item=True, allow_reuse=True)
    def check_values_not_empty(cls, v):
        assert v != '', 'Empty strings are not allowed.'
        return v

class Posts(BaseModel):
    __root__: List[Post]
