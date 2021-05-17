from datetime import datetime

from pydantic import BaseModel


class BaseJobModel(BaseModel):
    title: str
    description: str
    salary_from: int
    salary_to: int
    is_active: bool = True


class JobModel(BaseJobModel):
    id: int
    user_id: int
    create_at: datetime
    update_at: datetime


class JobInModel(BaseJobModel):
    pass
