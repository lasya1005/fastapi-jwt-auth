# app/auth/auth_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from app.crud.user_crud import verify_user_login
from app.auth.jwt_handler import create_access_token
from pydantic import BaseModel

# Initialize the router
router = APIRouter()

# Define the Login Request Model
class LoginRequest(BaseModel):
    username: str
    password: str

# Define the Login Response Model
class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# POST /login endpoint
@router.post("/login", response_model=LoginResponse)
async def login(login_request: LoginRequest):
    token = await verify_user_login(login_request.username, login_request.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return LoginResponse(access_token=token)

# POST /logout endpoint
@router.post("/logout")
async def logout():
    # In typical implementations, JWT tokens are stored client-side, so "logging out" is
    # often done by deleting the token on the client (frontend).
    # Alternatively, token blacklisting can be implemented if necessary.
    return {"message": "Logged out successfully"}
