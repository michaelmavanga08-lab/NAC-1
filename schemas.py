from datetime import date
from pydantic import BaseModel,ConfigDict
class ProjectCreate(BaseModel):
    name:str
    status:str="PLANNING"
    start_date:date|None=None
    end_date:date|None=None
class ProjectOut(ProjectCreate):
    id:int
    model_config=ConfigDict(from_attributes=True)
class TaskCreate(BaseModel):
    project_id:int
    parent_id:int|None=None
    name:str
    start_date:date|None=None
    end_date:date|None=None
    duration_days:int|None=None
    progress:float=0
    status:str="TODO"
    priority:str="MEDIUM"
class TaskOut(TaskCreate):
    id:int
    model_config=ConfigDict(from_attributes=True)
class ResourceCreate(BaseModel):
    project_id:int
    name:str
    resource_type:str
    quantity:float=1
    unit:str="unit"
class ResourceOut(ResourceCreate):
    id:int
    model_config=ConfigDict(from_attributes=True)
