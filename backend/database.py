from models import Recipe
from password import getPassword
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(getPassword())
db = client.RecipeApp
collection = db.SavedRecipes

async def get_saved_recipes():
    savedRecipes = []
    cursor = collection.find({}).limit(50)
    async for document in cursor:
        savedRecipes.append(Recipe(**document))
    return savedRecipes

async def get_recipes_by_user(user):
    savedRecipes = []
    cursor = collection.find({'user': user})
    async for document in cursor:
        savedRecipes.append(Recipe(**document))
    return savedRecipes

async def create_recipe(recipe):
    document = recipe
    result = await collection.insert_one(document)
    return document

async def delete_recipe(name):
    await collection.delete_one({'name': name})
    return True

