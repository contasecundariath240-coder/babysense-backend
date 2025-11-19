from fastapi import APIRouter
from .babies import router as babies_router
from .measurements import router as measurements_router

router = APIRouter()

router.include_router(babies_router, prefix="/babies", tags=["Babies"])
router.include_router(measurements_router, prefix="/measurements", tags=["Measurements"]) 
