"""NAC API routers."""
from .projects import router as projects_router
from .tasks import router as tasks_router
from .resources import router as resources_router

__all__ = ["projects_router", "tasks_router", "resources_router"]
