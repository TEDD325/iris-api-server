# app/schemas/request.py
from pydantic import BaseModel, Field


class IrisReq(BaseModel):
   sepal_length: float = Field(..., example=5.1, 
                         description="Sepal length") # 선택값
   sepal_width: float = Field(..., example=3.5, 
                          description="Sepal width") # 선택값
   petal_length: float = Field(..., example=1.4, 
                         description="Petal length") # 선택값
   petal_width: float = Field(..., example=0.2, 
                          description="Petal width") # 선택값
   # swagger에서 확인 가능