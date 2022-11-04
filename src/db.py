from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


DeclarativeBase = declarative_base()

noRepr = []
class RepresentableTable():
    def __repr__(self):
        keys = [elem for elem in vars(type(self)).keys() if not elem.startswith("_") and elem not in noRepr]
        keys = ["__tablename__"] + keys
        output = [f"{key}: {repr(getattr(self, key))}" for key in keys]
        return "\n".join(output)
        

class Database:
    def __init__(self, Session):
        self.Session = Session

    def with_session(function):
        def wrapper(self, *args, **kwargs):
            session = None
            result = None

            try:
                session = self.Session()
                result = function(self, session=session, *args, **kwargs)
            except Exception as ex:
                print(ex)
                if session is not None:
                    session.rollback()
            if session is not None:
                session.close()

            return result
        return wrapper
    

    @with_session
    def get(self, value, object, by, session=None):
        return session.query(object).filter(by == value).first()

    @with_session
    def add(self, object, *, session=None):
        session.add(object)
        session.commit()

    @with_session
    def delete(self, value, object, by, session=None):
        obj = session.query(object).filter(by == value).first()
        if obj is not None:
            session.delete(obj)
            session.commit()

    @with_session
    def update(self, value, new_object, by, session=None):
        obj = session.query(type(new_object)).filter(by == value).first()
        
        if obj is not None:
            # gets public object class' fields
            keys = [elem for elem in vars(type(new_object)).keys() if not elem.startswith("_") and elem != "id"]
            
            for key in keys:
                if hasattr(obj, key):
                    setattr(obj, key, getattr(new_object, key))

            session.commit()

    @with_session
    def append_child(self, value, childfield, child, object, by, obj=None, session=None):
        if obj is None:
            obj = session.query(object).filter(by == value).first()
        
        if obj is not None:
            getattr(obj, childfield).append(child)
            session.commit()