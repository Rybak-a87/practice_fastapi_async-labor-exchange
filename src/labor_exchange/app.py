from fastapi import FastAPI
import uvicorn

from src.labor_exchange.database.conf_db import database
from src.labor_exchange.api import router


app = FastAPI(title="Биржа труда")
app.include_router(router=router)


@app.get("/")
async def home_page():
    message = {
        "author": "Rybak Alexander",
        "message": "Hello! This is application Labor Exchange."
            }
    return message


# подключение приложения к базе данных
@app.on_event("startup")    # выполняет функцию во время старта приложения
async def startup():
    await database.connect()


@app.on_event("shutdown")    # выполняет функцию во время окончания работы подключения приложения
async def shutdown():
    await database.disconnect()
# подключение приложения к базе данных


# вызов uvicorn из основного файла app.py
if __name__ == "__main__":
    uvicorn.run(
        "src.labor_exchange.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
