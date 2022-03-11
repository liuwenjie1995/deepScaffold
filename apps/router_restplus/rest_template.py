import requests

from .baseRestful import BaseRestful
from tools.projectlog import logger
from flask_restplus import reqparse, Api
from flask_restplus import fields
from flask import Blueprint

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')  # 蓝图，用于加入app路由

api = Api(api_v1, version='1.0', title="API", description='a simple API')

ns = api.namespace('simple', description='a simple namespace')  # 给api起名
put_model = api.model('User',  # 设计model格式，确定输出和返回的json格式
                      {
                          'uid': fields.Integer,
                          'name': fields.String,
                          'age': fields.String,
                          'img': fields.String
                      })

normal_response = {
                          'res': fields.Integer(required=True),
                          'msg': fields.String(required=True),
                          'Info': {}
                      }

'''
parser 添加location = form 放在form表单内　
parser location 默认放在网址后
'''
get_args = api.parser()
get_args.add_argument('uid', type=int, required=True, help='用户id')
get_args.add_argument('name', type=str, required=True, help='用户名')

post_args = api.parser()
post_args.add_argument('uid', type=int, required=True, help='用户id', location='form')  # form形式不能用于get请求
post_args.add_argument('name', type=str, required=True, help='用户名', location='form')
post_args.add_argument('age', type=str, required=False, help='年龄', location='form')
post_args.add_argument('img', type=str, required=False, help='图片', location='form')


@ns.route('/user')
class UserRest(BaseRestful):
    @logger.catch()  # catch 方法帮助log载入日志
    @api.doc(description="get args connection",
             parser=get_args  # 添加参数
             )
    def get(self, **kwargs):
        return 'get'

    @api.expect(put_model, validate='True')
    @api.doc(description="post form connection",
             parser=post_args,
             responses={200: '成功',
                        400: '未获取文件'})
    def post(self, **kwargs):
        return 'post'

    @logger.catch()
    @api.doc(description="put form connection",
             # parser=put_args,  #传form格式需求
             # body=put_model    #传json格式需求
             # responses={200: '成功',
             #            400: '未获取文件'}
             )
    @api.marshal_with(put_model)  # 期望的返回json格式
    def put(self):
        put_info = post_args.parse_args()
        model = {
            'uid': put_info['uid'],
            'name': put_info['name'],
            'age': put_info['age'],
            'img': put_info['img']
        }
        print(model)
        return model
