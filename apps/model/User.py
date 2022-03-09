from db.sqlorm import *


class UserOrm(Base):
    __tablename__ = 'User'
    uid = Column(Integer, primary_key=True, unique=True)
    name = Column(String(32))
    age = Column(Integer)
    img = Column(String(32))

    def __repr__(self):
        tpl = "User(uid={},name={},age={}, img={})"
        return tpl.format(self.uid, self.name, self.age, self.img)


class UserMode(BaseModel):
    uid: int
    name: constr(max_length=20)
    age: Optional[int]
    img: Optional[constr(max_length=50)]

    class Config:
        orm_mode = True


@logger.catch()
def create_user(uid, name, age, img):
    user = UserOrm(uid=uid, name=name, age=age, img=img)
    print("[creating format]", UserMode.from_orm(user))
    return user

