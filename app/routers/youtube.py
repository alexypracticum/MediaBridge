from fastapi import APIRouter

from app.schemas.youtube import (
    DownloadRequest,
    DownloadResponse,
)
from app.services.youtube import YoutubeService

from app.schemas.job import JobResponse

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

@router.post(
    "/download",
    response_model=JobResponse,
)
def download(request: DownloadRequest):

    return service.download(request.url)

