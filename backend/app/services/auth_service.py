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

        # Check password is NOT the same as username (security best practice)
        if data.password.lower() == data.username.lower():
            raise HTTPException(
                status_code=400,
                detail="Password must be different from your username",
            )

        # Check password uniqueness across all users (best-effort, non-blocking)
        try:
            result = await db.execute(select(User))
            all_users = result.scalars().all()
            for existing_user in all_users:
                try:
                    if existing_user.hashed_password and verify_password(data.password, existing_user.hashed_password):
                        raise HTTPException(
                            status_code=400,
                            detail="This password is already in use by another account",
                        )
                except ValueError:
                    # Skip users with corrupted/invalid password hashes
                    continue
        except Exception:
            # If the check fails for any reason, don't block registration
            pass

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
