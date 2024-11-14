from app.crud.user_crud import create_user
import asyncio

async def create_admin():
    await create_user({"email": "admin@example.com", "username": "admin", "password": "admin123", "role": "admin"})

if __name__ == "__main__":
    asyncio.run(create_admin())
