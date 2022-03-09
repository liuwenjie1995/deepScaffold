from abc import abstractmethod, ABCMeta
from db.sqlorm import get_session


class BaseService:
    def __init__(self):
        self.session = get_session()

    def add(self, obj):
        self.session.add(obj)

    def change(self, obj):
        self.session.add(obj)

    def delete(self, obj):
        self.session.delete(obj)

    def finish(self):
        self.session.commit()


