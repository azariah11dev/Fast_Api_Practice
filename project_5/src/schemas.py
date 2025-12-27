from pydantic import BaseModel


class Post_Format(BaseModel):
    title: str
    content: str
    location: str