from pydantic import BaseModel

class Create_Post(BaseModel):
    title: str
    content: str