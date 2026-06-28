from app.models.download_job import DownloadJob


class JobManager:

    def __init__(self):
        self.jobs: dict[str, DownloadJob] = {}

    def add(self, job: DownloadJob):
        self.jobs[job.id] = job

    def get(self, job_id: str) -> DownloadJob | None:
        return self.jobs.get(job_id)

    def all(self) -> list[DownloadJob]:
        return list(self.jobs.values())

    def update_status(self, job_id: str, status: str):
        job = self.get(job_id)

        if job:
            job.status = status

    def update_progress(self, job_id: str, progress: float):
        job = self.get(job_id)

        if job:
            job.progress = progress

    def finish(self, job_id: str):
        job = self.get(job_id)

        if job:
            job.status = "finished"
            job.progress = 100

    def fail(self, job_id: str, error: str):
        job = self.get(job_id)

        if job:
            job.status = "failed"
            job.error = error


job_manager = JobManager()

