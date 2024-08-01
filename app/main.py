from fastapi import FastAPI
from app.api.member import auth_kis, auth_kakao, user

app = FastAPI()

# 라우터 추가
app.include_router(auth_kis.router, prefix="/auth_kis", tags=["auth_KIS"])
app.include_router(auth_kakao.router, prefix="/auth_kakao", tags=["auth_Kakao"])
app.include_router(user.router, prefix="/user", tags=["user"])
