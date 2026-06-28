from uuid import uuid4

from app.core.logging import logger

from app.utils.process import run_command 

from app.utils.commands import build_ytdlp_command

class YoutubeService:

    def download(self, url: str):

        job_id = str(uuid4())

        logger.info("Download requested")
        logger.info("Job ID : %s", job_id)
        logger.info("URL    : %s", url)

        command = build_ytdlp_command(url)

        result = run_command(command)

        logger.info("Return code: %s", result.returncode)
        logger.info("STDOUT: %s", result.stdout)
        logger.info("STDERR: %s", result.stderr)

        return {
        "job_id": job_id,
        "status": "queued",
        }