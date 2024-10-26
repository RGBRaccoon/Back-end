from fastapi import APIRouter
from api.handler.test import test_router
total_test_router= APIRouter()

total_test_router.include_router(router=test_router, prefix="/test")