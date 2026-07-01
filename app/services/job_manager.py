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
    
    def update_metadata(self, job_id: str, **kwargs):
        job = self.get(job_id)

        if job:
            for key, value in kwargs.items():
                setattr(job, key, value)


job_manager = JobManager()

