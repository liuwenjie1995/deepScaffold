from .Model import *


class UserOrm(Base):
    __tablename__ = 'table'
    id = Column(Integer, primary_key=True, )
    name = Column(String(32))
    age = Column(Integer)
    img = Column(String(32))


class UserMode(BaseModel):
    id: int
    name: constr(max_length=20)
    age: Optional[int]
    img: Optional[constr(max_lenght=50)]


@logger.catch()
def create(id, name, age, img):
    print(UserMode.from_orm(UserOrm(id, name, age, img)))

