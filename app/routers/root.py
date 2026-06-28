from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/")
def root():
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
    }
    