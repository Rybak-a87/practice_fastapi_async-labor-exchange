from typing import List, Optional

from datetime import datetime

from . import BaseService
from ..models.jobs import JobModel, JobInModel
from ..database.jobs import JobDB


class JobService(BaseService):
    job_db = JobDB.__table__

    async def create_job(self, user_id: int, job: JobInModel) -> JobModel:
        """добавить вакансию"""
        new_job = JobModel(
            id=0,
            title=job.title,
            description=job.description,
            salary_from=job.salary_from,
            salary_to=job.salary_to,
            is_active=job.is_active,
            user_id=user_id,
            create_at=datetime.utcnow(),
            update_at=datetime.utcnow()
        )
        values = {**new_job.dict()}    # значение для вставки
        values.pop("id", None)
        query = self.job_db.insert().values(**values)
        new_job.id = await self.database.execute(query=query)
        return new_job

    async def update_job(self, id: int, user_id, job: JobInModel) -> JobModel:
        """обновить - изменить вакансию"""
        update_job = JobModel(
            id=id,
            title=job.title,
            description=job.description,
            salary_from=job.salary_from,
            salary_to=job.salary_to,
            is_active=job.is_active,
            user_id=user_id,
            create_at=datetime.utcnow(),
            update_at=datetime.utcnow()
        )
        values = {**update_job.dict()}
        values.pop("id", None)
        values.pop("create_at", None)
        query = self.job_db.update().where(self.job_db.c.id == id).values(**values)
        await self.database.execute(query=query)
        return update_job

    async def delete_job(self, id: int) -> JobModel:
        """удалить вакансию"""
        query = self.job_db.delete().where(self.job_db.c.id == id)
        return await self.database.execute(query=query)

    async def get_list_jobs(self, limit: int = 100, skip: int = 0) -> List[JobModel]:
        """Получить список вакансий"""
        query = self.job_db.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_job_by_id(self, id: int) -> Optional[JobModel]:
        query = self.job_db.select().where(self.job_db.c.id == id)
        job = await self.database.fetch_one(query=query)
        if job is None:
            return None
        return JobModel.parse_obj(job)
