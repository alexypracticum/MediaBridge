from app.core.logging import logger
from app.services.job_manager import job_manager
from app.utils.commands import build_ytdlp_command
from app.models.download_job import DownloadJob
from app.utils.process import start_process
from pathlib import Path

def parse_metadata(line: str) -> dict:

    metadata = {}

    if "[download]" in line:

        
        if line.startswith("[download] Downloading playlist: "):
            metadata["playlist_title"] = line.removeprefix(
                "[download] Downloading playlist: "
            ).strip()

        # Добавляем запятых
        parts = line.split()

        logger.info(parts)

        if (
            len(parts) >= 6
            and parts[1] == "Downloading"
            and parts[2] == "item"
        ):
            metadata["playlist_index"] = int(parts[3])
            metadata["playlist_count"] = int(parts[5])

        if (
            len(parts) > 1
            and parts[1].endswith("%")
        ):
            metadata["progress"] = float(
                parts[1].replace("%", "")
            )
            if "ETA" in parts:
                metadata["speed"] = parts[5]
                metadata["eta"] = parts[7]

    if line.startswith("[download] Destination: "):

        filepath = line.removeprefix(
            "[download] Destination: "
        ).strip()

        metadata["filepath"] = filepath
        metadata["title"] = Path(filepath).stem

    return metadata

class Downloader:

    def download(self, job: DownloadJob):
        job_manager.update_metadata(job.id, status="running")

        command = build_ytdlp_command(job.url)

        # разбивка на задачи
        logger.info("Starting download (Job: %s)", job.id)

        process = start_process(command)

        # красивый лог
        for line in process.stdout:  # Пока процесс работает, каждый раз, когда появилась новая строка, отдай её мне.
            
            logger.info(line.rstrip())

            metadata = parse_metadata(line)

            if metadata:
                job_manager.update_metadata(job.id, **metadata)

        process.wait()

        logger.info("Return code: %s", process.returncode)

        if process.returncode == 0:
            job_manager.update_metadata(
                job.id,
                status="finished",
                progress=100,
            )
        else:
            job_manager.update_metadata(
                job.id,
                status="failed",
                error="Download failed",
            )

downloader = Downloader()
