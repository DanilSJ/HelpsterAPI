from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from core.config import settings
from api_v1 import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan,
    title="User Management API",
    description="API HelpsterAPI",
    version="0.1.0",
)
app.include_router(router=user_router, prefix=settings.api_v1_prefix)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
