import click
from model import User
from flask import Flask
from flask_restplus import Api
from base_interface.BaseResful import BaseRestful
from db.sqlorm import get_session, init_db, Base, engine
from tools.projectlog import logger
from service.userService import UserService
from router_view.main_view import mainpages

app = Flask(__name__)
app.register_blueprint(mainpages, url_prefix='/')
logger.info('----------------------------------------start db_conn----------------------------------------------------')
Base.metadata.create_all(engine)
session = get_session()
init_db()

logger.info('----------------------------------------start option-----------------------------------------------------')
api = Api(app, version='1.0', title="API", description='a simple API')
ns = api.namespace('simple', description='a simple namespace')
SWAGGER_URL = '/api/docs'
API_URL = 'http://localhost/v2/swagger.json'  # Our API url (can of course be a local resource)

logger.info('--------------------------------------------view---------------------------------------------------------')


@app.route("/")
@app.route("/hello")
def hello_world():
    return "hello_world"


logger.info('--------------------------------------------interface----------------------------------------------------')


@ns.route('/v1/app/<string:name>')
class UserView(BaseRestful):

    @logger.catch()
    def get(self, uid, name, age, img):
        user = User.create_user(uid, name, age, img)
        userService = UserService()
        userService.add(user)
        userService.finish()
        return 'get finish', uid

    def post(self, name):
        return 'post' + name


# --------------------------------------------------------start---------------------------------------------------------
@click.command()
@click.option("--port", default=8080)
@click.option("--host", default="0.0.0.0", type=str)
@click.option("--debug", default=True, type=bool)
def run(port, host, debug):
    app.run(port=port, host=host, debug=debug)


if __name__ == '__main__':
    run()
