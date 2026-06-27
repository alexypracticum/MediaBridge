from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.logging import logger


SEPARATOR = "=" * 50

def print_banner():
    logger.info(SEPARATOR)
    logger.info("%s %s", settings.app_name, settings.app_version)
    logger.info("")
    logger.info("Collect. Organize. Watch.")
    logger.info("")
    logger.info("Media Root : %s", settings.media_root)
    logger.info("Log Level  : %s", settings.log_level)
    logger.info("")
    logger.info("Server is ready.")
    logger.info(SEPARATOR)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print_banner()

    yield

    logger.info("MediaBridge stopped.")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
    }