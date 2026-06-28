from datetime import datetime
from uuid import uuid4

from app.models.download_job import DownloadJob
from app.services.job_manager import job_manager
from app.services.downloader import downloader

from threading import Thread

class YoutubeService:

    def download(self, url: str):

        job = DownloadJob(
            id=str(uuid4()),
            url=url,
            status="queued",
            created_at=datetime.now(),
        )

        job_manager.add(job)

        thread = Thread(
            target=downloader.download,
            args=(job,),
            daemon=True,
        )

        thread.start()

        return {
            "job_id": job.id,
            "status": job.status,
        }

        