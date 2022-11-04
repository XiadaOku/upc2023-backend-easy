from sqlalchemy import Column, Integer

from db import DeclarativeBase, RepresentableTable, noRepr


class Table(DeclarativeBase, RepresentableTable):
    __tablename__ = "aboba"
    id = Column(Integer, primary_key=True)

noRepr += ["id"]