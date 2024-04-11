from contextlib import asynccontextmanager # Python의 context manager 문법: with가 대표적. yield: 제어권을 호출한 쪽에 넘겨준 다음 실행하게 한다.
# Python context manager 문법에 대해 공부해야 함
from fastapi import FastAPI
from starlette.concurrency import run_in_threadpool

from app import routers
from app.core.model_registry import model_registry
from app.utils import load_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # model_registry.register_model('iris_model', load_model()) # load_model: blocking 연산. 

    model = await run_in_threadpool(load_model) # await: 비동기 연산임을 시스템에 알려준다.
    model_registry.register_model('iris_model', model) # load_model: blocking 연산. 

    yield

    model_registry.clear()


app = FastAPI(lifespan=lifespan)


app.include_router(routers.router) # 미리 정의한 라우터를 붙인다.

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "OK"}

