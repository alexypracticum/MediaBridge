from app.core.logging import logger
from app.services.job_manager import job_manager
from app.utils.commands import build_ytdlp_command
from app.models.download_job import DownloadJob
# from app.utils.process import run_command 
from app.utils.process import start_process


class Downloader:

    def download(self, job: DownloadJob):
        job_manager.update_status(job.id, "running")

        command = build_ytdlp_command(job.url)

        # разбивка на задачи
        logger.info("Starting download (Job: %s)", job.id)

        process = start_process(command)

        # красивый лог
        for line in process.stdout:  # Пока процесс работает, каждый раз, когда появилась новая строка, отдай её мне.
            
            if "[download]" in line:

                parts = line.split()

                if len(parts) < 2:
                    continue

                if not parts[1].endswith("%"):
                    continue

                progress = float(parts[1].replace("%", ""))

                job_manager.update_progress(job.id, progress)

                # logger.info("Progress: %s", progress)

                logger.info("DOWNLOAD LINE")
            
            logger.info(line.rstrip())

        process.wait()

        logger.info("Return code: %s", process.returncode)

        if process.returncode == 0:
            job_manager.finish(job.id)
        else:
            job_manager.fail(job.id, "Download failed")



downloader = Downloader()
