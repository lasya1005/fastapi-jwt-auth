from fastapi import Depends, HTTPException
from app.auth.jwt_handler import decode_access_token
from app.models import TokenData

async def role_based_access(token: str, role_required: str):
    token_data = decode_access_token(token)
    if token_data and token_data.role == role_required:
        return token_data
    raise HTTPException(status_code=403, detail="Insufficient permissions")
