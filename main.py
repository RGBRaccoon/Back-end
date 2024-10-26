from gunicorn.app.base import BaseApplication
from fastapi import FastAPI
import uvicorn

# FastAPI 애플리케이션 정의
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running with Gunicorn!"}

# Gunicorn의 BaseApplication을 상속하여 애플리케이션 클래스 정의
class CustomGunicornApp(BaseApplication):
    def __init__(self, app, options=None):
        self.app = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.app

# Gunicorn을 파이썬 코드로 실행하는 함수
def run_gunicorn():
    options = {
        "bind": "0.0.0.0:8000",  # 서버 바인딩 주소 및 포트
        "workers": 4,  # 워커 수
        "worker_class": "uvicorn.workers.UvicornWorker",  # Uvicorn ASGI 워커
        "loglevel": "info",  # 로그 레벨 설정
    }

    CustomGunicornApp(app, options).run()

if __name__ == "__main__":
    # Gunicorn 서버를 Python 코드 내에서 실행
    run_gunicorn()
