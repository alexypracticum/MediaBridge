from fastapi import APIRouter

from app.schemas.youtube import (
    DownloadRequest,
    DownloadResponse,
)
from app.services.youtube import YoutubeService

# Создаём сервис
service = YoutubeService()

router = APIRouter(
    prefix="/youtube",
    tags=["YouTube"]
)

# Маршрут
@router.post("/download")
def download(request: DownloadRequest):

    return service.download(request.url)

