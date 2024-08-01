from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import RedirectResponse
import requests
import logging


router = APIRouter()

AUTHORIZE_ENDPOINT = "https://kauth.kakao.com/oauth/authorize"
ACCESS_TOKEN_ENDPOINT = "https://kauth.kakao.com/oauth/token"

# 카카오 간편인증 - 인가 코드 받기
@router.get("/kakao/authorize")
def getAuthCode(redirect_uri: str = Query(..., alias="redirect_uri"), api_key: str = Query(..., alias="api_key")):
    logging.info("GET /getAuthCode called")

    # 카카오 인증 url로 get 요청
    try:
        ext_url = f"{AUTHORIZE_ENDPOINT}?response_type=code&client_id={api_key}&redirect_uri={redirect_uri}"
        logging.info(f"request url for kakao : {ext_url}")
        response = requests.get(ext_url)

        # API 응답 성공 여부 확인
        response.raise_for_status()

        return RedirectResponse(url=ext_url)
    except requests.RequestException as e:
        logging.error(f"카카오 인증 요청에 실패하였습니다 : {e}")
        raise HTTPException(status_code=500, detail="인증 실패")

# @router.get("/kakao/callback")