# Подключаем
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.logging import logger

from app.routers import root
from app.routers import youtube

from app.routers.jobs import router as jobs_router

# Наводим красоту
SEPARATOR = "=" * 50

# Баннер
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

# Вывод баннера
@asynccontextmanager
async def lifespan(app: FastAPI):
    print_banner()

    yield

    logger.info("MediaBridge stopped.")

# Фаст АПИ
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

# Роуты
app.include_router(root.router)
app.include_router(youtube.router)
app.include_router(jobs_router)
