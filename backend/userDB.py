from password import getPassword
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(getPassword())
db = client.RecipeApp
collection = db.Users

async def login(username):
    document = await collection.find_one({"username": username})
    return document

async def register(user):
    newUser = user
    result = await collection.insert_one(newUser)
    return newUser
