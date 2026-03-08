from fastapi import FastAPI
from api.routes.calculo import router

app = FastAPI()

app.include_router(router)