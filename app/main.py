from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="HIVE - Occupation Mapping Engine")

app.include_router(router)
