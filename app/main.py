from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers import analysis
from config import celery_app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    print("Application startup")
    celery_app.start()
    yield
    # Shutdown code
    print("Application shutdown")
    celery_app.stop()

app = FastAPI(lifespan=lifespan)
app.include_router(analysis.router, prefix="/api")
