from fastapi import APIRouter

from app.schemas.youtube import DownloadRequest
from app.services.youtube import download_video

router = APIRouter(
    prefix="/youtube",
    tags=["YouTube"]
)

# Маршрут
@router.post("/download")
def download(request: DownloadRequest):

    download_video(request.url)

    return {
        "status": "accepted"
    }
