from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse
from app.core.security import hash_password, verify_password, create_access_token

class AuthService:
    @staticmethod
    async def register(db: AsyncSession, data: UserCreate) -> TokenResponse:
        # Check existing username
        result = await db.execute(select(User).where(User.username == data.username))
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Username already exists")
        # Check existing email
        result = await db.execute(select(User).where(User.email == data.email))
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Email already registered")

        user = User(
            username=data.username,
            email=data.email,
            hashed_password=hash_password(data.password),
            full_name=data.full_name,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

        token = create_access_token({"sub": user.id, "role": user.role.value})
        return TokenResponse(
            access_token=token,
            user=UserResponse.model_validate(user),
        )

    @staticmethod
    async def login(db: AsyncSession, data: UserLogin) -> TokenResponse:
        result = await db.execute(select(User).where(User.username == data.username))
        user = result.scalar_one_or_none()
        if not user or not verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        if not user.is_active:
            raise HTTPException(status_code=403, detail="Account is inactive")

        token = create_access_token({"sub": user.id, "role": user.role.value})
        return TokenResponse(
            access_token=token,
            user=UserResponse.model_validate(user),
        )
