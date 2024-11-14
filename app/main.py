from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

db_client = AsyncIOMotorClient(settings.MONGO_URI)
database = db_client["resoluteAI"]
users_collection = database["users"]
