from flask_restplus import Api, Resource
from flask_restplus import fields


# GET用来获取资源
# POST用来新建资源（也可用于更新资源）
# PUT用来更新资源
# DELETE用来删除资源。


class AnyType(fields.Raw):
    def format(self, value):
        return value


class BaseRestful(Resource):

    def get(self):
        pass
