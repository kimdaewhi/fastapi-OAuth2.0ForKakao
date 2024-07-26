from fastapi import FastAPI
from app.api.v1 import member, auth

app = FastAPI()

# 라우터 추가
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(member.router, prefix="/members", tags=["members"])