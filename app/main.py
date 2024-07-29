from fastapi import FastAPI
from app.api.member import user, auth

app = FastAPI()

# 라우터 추가
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])