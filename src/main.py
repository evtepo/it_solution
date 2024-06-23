import uvicorn
from fastapi import FastAPI

from config.settings import settings
from api.v1.advertisement import router as advertisement_router


app = FastAPI(title=settings.project_name)

app.include_router(advertisement_router, prefix="/api/v1/advertisement", tags=["Advertisement"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.localhost,
        port=settings.localport,
    )
