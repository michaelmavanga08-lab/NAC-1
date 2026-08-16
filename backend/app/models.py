from sqlalchemy import String,Integer,Date,Float,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column
from .database import Base
class Project(Base):
    __tablename__="projects"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(200))
    status:Mapped[str]=mapped_column(String(30),default="PLANNING")
    start_date:Mapped[object|None]=mapped_column(Date,nullable=True)
    end_date:Mapped[object|None]=mapped_column(Date,nullable=True)
class Task(Base):
    __tablename__="tasks"
    id:Mapped[int]=mapped_column(primary_key=True)
    project_id:Mapped[int]=mapped_column(ForeignKey("projects.id"))
    parent_id:Mapped[int|None]=mapped_column(ForeignKey("tasks.id"),nullable=True)
    name:Mapped[str]=mapped_column(String(200))
    start_date:Mapped[object|None]=mapped_column(Date,nullable=True)
    end_date:Mapped[object|None]=mapped_column(Date,nullable=True)
    duration_days:Mapped[int|None]=mapped_column(Integer,nullable=True)
    progress:Mapped[float]=mapped_column(Float,default=0)
    status:Mapped[str]=mapped_column(String(30),default="TODO")
    priority:Mapped[str]=mapped_column(String(20),default="MEDIUM")
class Resource(Base):
    __tablename__="resources"
    id:Mapped[int]=mapped_column(primary_key=True)
    project_id:Mapped[int]=mapped_column(ForeignKey("projects.id"))
    name:Mapped[str]=mapped_column(String(200))
    resource_type:Mapped[str]=mapped_column(String(30))
    quantity:Mapped[float]=mapped_column(Float,default=1)
    unit:Mapped[str]=mapped_column(String(30),default="unit")
