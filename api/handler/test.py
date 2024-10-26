from fastapi import APIRouter

test_router = APIRouter()


@test_router.get("/hello")
async def print_hello():
    return "hello"
