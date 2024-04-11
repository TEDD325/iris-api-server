# app/schemas/response.py
from pydantic import BaseModel, Field


class IrisResp(BaseModel): # Response 모델의 일부
   target: int = Field(..., example=0, 
                       description="Predicted class")

class ResponseModel(BaseModel): # 실제 응답 모델
   status_code: int = Field(..., example=200, 
                           description="Status code")
   data: IrisResp = Field(..., # IrisResp의 정의를 따른다.
                         description="Response data")