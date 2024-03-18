from fastapi import APIRouter
from examples.example_01_button_click import router as button_click_router
from examples.example_02_counter import router as counter_router
from examples.example_03_trigger import router as trigger_router

router = APIRouter()
router.include_router(button_click_router, prefix="/example-01")
router.include_router(counter_router, prefix="/example-02")
router.include_router(trigger_router, prefix="/example-03")
