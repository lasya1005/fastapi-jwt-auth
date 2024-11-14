from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve MongoDB URI and Database Name from environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Initialize the MongoDB client and database
client = AsyncIOMotorClient(MONGODB_URI)
database = client[DATABASE_NAME]

# Define the users collection
users_collection = database["users"]
