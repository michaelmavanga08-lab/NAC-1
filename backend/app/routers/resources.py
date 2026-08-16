from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Project, Resource
from ..schemas import ResourceCreate, ResourceOut

router = APIRouter(prefix="/api/v1/resources", tags=["Resources"])


@router.post("", response_model=ResourceOut, status_code=201)
def create_resource(
    payload: ResourceCreate,
    db: Session = Depends(get_db),
):
    if db.get(Project, payload.project_id) is None:
        raise HTTPException(status_code=404, detail="Project not found")

    resource = Resource(**payload.model_dump())
    db.add(resource)
    db.commit()
    db.refresh(resource)
    return resource


@router.get("", response_model=list[ResourceOut])
def list_resources(
    project_id: int | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Resource)
    if project_id is not None:
        query = query.filter(Resource.project_id == project_id)
    return query.all()
