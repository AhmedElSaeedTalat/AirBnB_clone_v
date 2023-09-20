#!/usr/bin/python3
""" DBStorage: class from db storage """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ DBStorage: class from db storage """
    __engine = None
    __session = None

    def __init__(self):
        """ """
        usr = os.environ.get('HBNB_MYSQL_USER')
        ps = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        db = os.environ.get('HBNB_MYSQL_DB')
        statement = f"mysql+mysqldb://{usr}:{ps}@{host}/{db}"
        self.__engine = create_engine(f"{statement}",
                                      pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        my_dict = {}
        if cls is None:
            all_objs = self.__session.query(User, State, City,
                                            Amenity, Place, Review)\
                                     .all()
        else:
            all_objs = self.__session.query(cls).all()

        for obj in all_objs:
            my_dict[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return my_dict

    def new(self, obj):
        """ """
        self.__session.add(obj)

    def save(self):
        """ """
        self.__session.commit()

    def delete(self, obj=None):
        """ """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ """
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
