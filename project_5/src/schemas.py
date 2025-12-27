from pydantic import BaseModel


class Item(BaseModel):
    title: str
    content: str
    location: str