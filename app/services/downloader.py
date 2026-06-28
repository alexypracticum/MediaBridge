from app.core.logging import logger
from app.services.job_manager import job_manager
from app.utils.commands import build_ytdlp_command
from app.models.download_job import DownloadJob
from app.utils.process import run_command 


class Downloader:

    def download(self, job: DownloadJob):
        job_manager.update_status(job.id, "running")

        command = build_ytdlp_command(job.url)

        result = run_command(command)

        logger.info("Job ID : %s", job.id)

        logger.info("Return code: %s", result.returncode)
        logger.info("STDOUT: %s", result.stdout)
        logger.info("STDERR: %s", result.stderr)

        if result.returncode == 0:
            job_manager.finish(job.id)
        else:
            job_manager.fail(job.id, result.stderr)


downloader = Downloader()
