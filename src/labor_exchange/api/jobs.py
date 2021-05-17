from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from ..models.users import UserModel
from ..services.jobs import JobService
from ..models.jobs import JobModel, JobInModel
from .depends import get_job_service, get_current_user


router = APIRouter()


@router.post("/create-job", response_model=JobModel)
async def create_job(
        job: JobInModel,
        current_user: UserModel = Depends(get_current_user),
        job_service: JobService = Depends(get_job_service)
):
    """
    ## Добавить вакансию
    """
    return await job_service.create_job(user_id=current_user.id, job=job)


@router.put("/update-job", response_model=JobModel)
async def update_job(
        id: int,
        job: JobInModel,
        current_user: UserModel = Depends(get_current_user),
        job_service: JobService = Depends(get_job_service)
):
    """
    ## Обновить - изменить вакансию
    """
    old_job = await job_service.get_job_by_id(id=id)
    if old_job is None or old_job.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")

    return await job_service.update_job(id=id, user_id=current_user.id, job=job)


@router.delete("/delete-job")
async def delete_job(
        id: int,
        current_user: UserModel = Depends(get_current_user),
        job_service: JobService = Depends(get_job_service)
):
    """
    ## Удалить вакансию
    """
    exc = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    job = await job_service.get_job_by_id(id=id)
    if job is None or job.user_id != current_user.id:
        raise exc
    result = await job_service.delete_job(id=id)
    return {"status": True}


@router.get("/list-jobs", response_model=List[JobModel])
async def get_list_jobs(
        limit: int = 100,
        skip: int = 0,
        job_service: JobService = Depends(get_job_service)
):
    """
    ## Получить список вакансий
    """
    return await job_service.get_list_jobs(limit=limit, skip=skip)
