import os
import base64
from .baseRestful import BaseRestful, AnyType
from tools.projectlog import logger
from flask_restplus import reqparse, Api
import copy
from flask_restplus import fields
from flask import Blueprint

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')  # 蓝图，用于加入app路由

api = Api(api_v1, version='1.0', title="API", description='a simple API')

ns = api.namespace('background_change', description='a simple namespace')  # 给api起名

normal_response = api.model("Model", {
    'res': fields.Integer(required=True),
    'msg': fields.String(required=True),
    'Info': AnyType(required=True)
})

response = {
    'res': 1,
    'msg': 'success',
    'Info': {}
}


@ns.route('/frames')
class GreenMode(BaseRestful):
    @logger.catch()
    @api.doc(description='获取视频流')
    def get(self):
        return 1


@ns.route('/green_mode/<int:mode>')
class GreenMode(BaseRestful):
    @logger.catch()
    @api.doc(description='获取绿幕状态')
    @api.marshal_with(normal_response)  # 期望的返回json格式
    def get(self, mode):
        res = copy.deepcopy(response)
        res['Info'] = {}
        return res


bg_post_parser = api.parser()
bg_post_parser.add_argument('id', type=str, required=True, help='图片id')

bg_put_parser = api.parser()
bg_put_parser.add_argument('rgb', type=str, required=True, help='颜色')


@ns.route('/background')
class Background(BaseRestful):
    @logger.catch()
    @api.doc(description='获取图片list')
    @api.marshal_with(normal_response)
    def get(self):
        mdict = {}
        root_path = r'C:\Users\liu\PycharmProjects\deepScaffold\apps\static\imgs\background'
        img_path_list = os.listdir(root_path)

        for index, img_path in enumerate(img_path_list):
            with open(os.path.join(root_path, img_path), "rb") as f:
                img_b64 = str(base64.b64encode(f.read()), encoding='utf-8')
                mdict[index] = {'type': 'img', 'resource': img_b64}
                if index is 8:
                    mdict[9] = {'type': 'video', 'resource': img_b64}
        res = copy.deepcopy(response)
        res['Info'] = mdict
        return res

    @logger.catch()
    @api.doc(description='获取指定图片',
             parser=bg_post_parser
             )
    @api.marshal_with(normal_response)
    def post(self):
        args = bg_post_parser.parse_args()
        res = copy.deepcopy(response)
        res['Info'] = {'img_id': args['id']}
        return res

    @logger.catch()
    @api.doc(description='删除指定图片',
             parser=bg_post_parser
             )
    @api.marshal_with(normal_response)
    def delete(self):
        args = bg_post_parser.parse_args()
        res = copy.deepcopy(response)
        res['Info'] = {'img_id': args['id']}
        return res

    @logger.catch()
    @api.doc(description='获取指定颜色',
             parser=bg_put_parser
             )
    @api.marshal_with(normal_response)
    def put(self):
        args = bg_put_parser.parse_args()
        res = copy.deepcopy(response)
        res['Info'] = {'rgb': args['rgb']}
        return res
