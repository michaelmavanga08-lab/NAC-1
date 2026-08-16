from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from .database import Base,engine,get_db
from .models import Project,Task,Resource
from .schemas import ProjectCreate,ProjectOut,TaskCreate,TaskOut,ResourceCreate,ResourceOut
Base.metadata.create_all(bind=engine)
app=FastAPI(title="NAC API",version="3.3.16")
@app.get("/health")
def health(): return {"status":"ok","product":"NAC","version":"3.3.16"}
@app.post("/api/v1/projects",response_model=ProjectOut,status_code=201)
def create_project(p:ProjectCreate,db:Session=Depends(get_db)):
    x=Project(**p.model_dump()); db.add(x); db.commit(); db.refresh(x); return x
@app.get("/api/v1/projects",response_model=list[ProjectOut])
def projects(db:Session=Depends(get_db)): return db.query(Project).all()
@app.post("/api/v1/tasks",response_model=TaskOut,status_code=201)
def create_task(p:TaskCreate,db:Session=Depends(get_db)):
    if not db.get(Project,p.project_id): raise HTTPException(404,"Project not found")
    x=Task(**p.model_dump()); db.add(x); db.commit(); db.refresh(x); return x
@app.get("/api/v1/tasks",response_model=list[TaskOut])
def tasks(project_id:int|None=None,db:Session=Depends(get_db)):
    q=db.query(Task)
    return q.filter(Task.project_id==project_id).all() if project_id else q.all()
@app.post("/api/v1/resources",response_model=ResourceOut,status_code=201)
def create_resource(p:ResourceCreate,db:Session=Depends(get_db)):
    if not db.get(Project,p.project_id): raise HTTPException(404,"Project not found")
    x=Resource(**p.model_dump()); db.add(x); db.commit(); db.refresh(x); return x
@app.get("/api/v1/resources",response_model=list[ResourceOut])
def resources(project_id:int|None=None,db:Session=Depends(get_db)):
    q=db.query(Resource)
    return q.filter(Resource.project_id==project_id).all() if project_id else q.all()
