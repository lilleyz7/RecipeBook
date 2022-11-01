from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    imageUrl: str
    ingredients: list
    steps: list
    dishType: str
    user: str

class User(BaseModel):
    email: str
    username: str
    password: str