from .Model import *


class User(Base):
    __tablename__ = 'table'
    id = Column(Integer, primary_key=True, )
    name = Column(String(32))
    age = Column(Integer)
    img = Column(String(32))
