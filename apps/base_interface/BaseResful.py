import abc

from flask_restplus import Api, Resource
from abc import ABCMeta, abstractmethod


# GET用来获取资源
# POST用来新建资源（也可用于更新资源）
# PUT用来更新资源
# DELETE用来删除资源。

class BaseRestful(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
