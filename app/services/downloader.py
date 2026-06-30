from app.core.logging import logger
from app.services.job_manager import job_manager
from app.utils.commands import build_ytdlp_command
from app.models.download_job import DownloadJob
from app.utils.process import start_process
from pathlib import Path

def parse_metadata(line: str) -> dict:

    metadata = {}

    if "[download]" in line:

        parts = line.split()

        if (
            len(parts) > 1
            and parts[1].endswith("%")
        ):
            metadata["progress"] = float(
                parts[1].replace("%", "")
            )

    if line.startswith("[download] Destination: "):

        filepath = line.removeprefix(
            "[download] Destination: "
        ).strip()

        metadata["filepath"] = filepath
        metadata["title"] = Path(filepath).stem

    return metadata

class Downloader:

    def download(self, job: DownloadJob):
        job_manager.update_status(job.id, "running")

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
            job_manager.finish(job.id)
        else:
            job_manager.fail(job.id, "Download failed")

downloader = Downloader()
