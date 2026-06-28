from fastapi import APIRouter

from app.services.job_manager import job_manager

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get("/")
def list_jobs():
    return job_manager.all()