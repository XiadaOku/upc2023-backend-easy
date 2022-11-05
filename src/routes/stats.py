from fastapi import APIRouter

from src.init import db
from src.tables import Shifts


router = APIRouter()

@router.get("/stats")
async def get_stats():
    return [{"rot": item.rot, "usages": item.usages} for item in db.get_all(Shifts)]