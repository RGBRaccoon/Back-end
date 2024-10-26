from fastapi import FastAPI
from config.fastapi_config import CustomGunicornApp
from api.router.test_router import total_test_router

# FastAPI 애플리케이션 정의


app = FastAPI()
app.include_router(router=total_test_router)
if __name__ == "__main__":
    # Gunicorn 서버를 Python 코드 내에서 실행
    CustomGunicornApp(app=app).run()
