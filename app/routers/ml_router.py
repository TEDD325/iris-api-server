import pandas as pd
from fastapi import APIRouter

from app.schemas.request import IrisReq
from app.schemas.response import ResponseModel, IrisResp
from app.core.model_registry import model_registry
# core: 서버에서 관리할 환경 변수, model_registry, 담아놓을, 모아놓을 것들

router = APIRouter()


@router.post("/predict", response_model=ResponseModel) 
def predict(request: IrisReq): # async가 아닌 sync인 이유는, predict 연산이 동기화 방식이기 때문이다->별도의 thread pool에서 돌게 된다.
   result = model_registry.get_model("iris_model").predict(
       pd.DataFrame([request.model_dump()])
   )

   return ResponseModel(status_code=200, data=IrisResp(target=result))
