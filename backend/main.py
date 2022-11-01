from fastapi import FastAPI, HTTPException
from models import Recipe, User

from database import (
    create_recipe,
    delete_recipe,
    get_saved_recipes,
    get_recipes_by_user
)

from userDB import (
    login,
    register
)

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def read_root():
    return {'Howdy': 'Paw'}


@app.get('/generic')
async def get_all_saved():
    response = await get_saved_recipes()
    return response

@app.get('/generic/{user}')
async def get_users_saves(user):
    response = await get_recipes_by_user(user)
    return response


@app.get('/login/{username}', response_model=User)
async def attempt_login(username):
    response = await login(username)
    if response:
        return response
    else:
        raise HTTPException(404, f"There is no user with {username} or incorrect pass")


@app.post('/add_recipe', response_model=Recipe)
async def post_recipe(recipe: Recipe):
    response = await create_recipe(dict(recipe))
    if response:
        return response
    else:
        raise HTTPException(400, "Unable to process request")


@app.post('/register_user', response_model=User)
async def register_user(user: User):
    response  = await register(dict(user))
    if response:
        return response
    else:
        raise HTTPException(400, "Unable to process request")
    

@app.delete('/remove_recipe/{name}')
async def remove_recipe(name):
    response = await delete_recipe(name)
    if response:
        return 'Removed Successfully'
    else:
        raise HTTPException(404, f"No recipe with the name {name}")





