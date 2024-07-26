from datetime import date
from pydantic import BaseModel

class MemberBase(BaseModel):
    access_token: str
    expired_date: date
    access_token_type: str
    expires_in: int

class MemberCreate(MemberBase):
    pass

class MemberResponse(MemberBase):
    class Config:
        orm_mode = True
