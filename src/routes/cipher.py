from fastapi import APIRouter

from src.init import db
from src.tables import Shifts
from src.models.cipher import EncodeModel


router = APIRouter()

@router.post("/encode")
async def post_encode(data: EncodeModel) -> str:
    update_rot(data.rot)
    return caesar_encode(data.message, data.rot)

@router.get("/decode")
async def get_decode(message: str, rot: int) -> str:
    update_rot(rot)
    return caesar_encode(message, 26 - rot)


def update_rot(rot: int):
    rot_stats = db.get(rot, by=Shifts.rot, object=Shifts)
    if rot_stats is None:
        db.add(Shifts(rot=rot, usages=1))
    else:
        db.update(rot_stats, {"usages": rot_stats.usages + 1})

def caesar_encode(message: str, rot: int) -> str:
    result = ""
    for char in message:
        if char.isalpha():
            alph_start = ord("aA"[char.isupper()])
            encoded_letter = (ord(char) - alph_start + rot) % 26
            result += chr(alph_start + encoded_letter)
        else:
            result += char
    return result