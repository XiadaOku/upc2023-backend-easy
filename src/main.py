from fastapi import FastAPI

from src.init import engine, DeclarativeBase
from src.routes import cipher, stats


DeclarativeBase.metadata.create_all(bind=engine)
DeclarativeBase.metadata.bind = engine

app = FastAPI()
app.include_router(cipher.router)
app.include_router(stats.router)