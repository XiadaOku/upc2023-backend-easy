from sqlalchemy import Column, Integer

from src.db import DeclarativeBase, RepresentableTable


class Shifts(DeclarativeBase, RepresentableTable):
    __tablename__ = "shifts"
    RepresentableTable.noRepr += ["id"]
    id = Column(Integer, primary_key=True)
    rot = Column(Integer)
    usages = Column(Integer)