from fastapi import APIRouter
from .demo import router as demo_router


router = APIRouter()

router.include_router(
    demo_router,
    prefix='/demo',
    tags=['demo'],
)