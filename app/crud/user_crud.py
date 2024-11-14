from app.auth.jwt_handler import create_access_token
from app.database import users_collection  # Import users_collection from database.py
import bcrypt

async def create_user(user_data):
    # Hash the password before storing
    hashed_password = bcrypt.hashpw(user_data["password"].encode('utf-8'), bcrypt.gensalt())
    user_data["password"] = hashed_password
    await users_collection.insert_one(user_data)

async def verify_user_login(username, password):
    # Fetch the user from the database
    user = await users_collection.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        # If password matches, generate and return an access token
        return create_access_token({"username": user["username"], "role": user["role"]})
    return None
