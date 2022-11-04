from init import engine, db, DeclarativeBase
from tables import Table


# DeclarativeBase.metadata.reflect(bind=engine)
# DeclarativeBase.metadata.drop_all(bind=engine)
DeclarativeBase.metadata.create_all(bind=engine)
DeclarativeBase.metadata.bind = engine