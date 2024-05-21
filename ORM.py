from derectoria import database
from derectoria.database import Base, engine
from derectoria import models 

class ORM:
    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)
        

    @staticmethod
    def drop_tables():
        Base.metadata.drop_all(engine)

    @staticmethod
    def add_record(record):
        with session_factory() as session:
            session.add(record)
            session.commit()

    @staticmethod
    def get_all_users():
        with session_factory() as session:
            users = session.query(User).all()
            return users