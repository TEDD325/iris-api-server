from fastapi import APIRouter
from app.routers import ml_router # predict 정의한 라우터 가져오기

router = APIRouter()

router.include_router(ml_router.router, 
                      prefix = '/v1/ml', 
                      tags=['ml'])

