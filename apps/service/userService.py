from .baseService import BaseService
from tools import projectlog
logger = projectlog.logger


@logger.catch()
class UserService(BaseService):
    def __init__(self):
        super().__init__()

    def add(self, obj):
        super().add(obj)

    def change(self, obj):
        super().change(obj)

    def delete(self, obj):
        super().delete(obj)

    def finish(self):
        super().finish()
