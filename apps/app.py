import click
import time
from flask import Flask
from flask_restplus import Resource, Api
from base_interface.BaseResful import BaseRestful
from model.Model import get_session, init_db, drop_db
from configs.config import MODE, config
from tools.projectlog import logger
app = Flask(__name__)
logger.info('----------------------------------start project-------------------------------------')
logger.info('create db')
init_db()
session = get_session()

# ------------------------------------------------------option---------------------------------------------------------
logger.add('start option')
api = Api(app, version='1.0', title="API", description='a simple API')
ns = api.namespace('simple', description='a simple namespace')
SWAGGER_URL = '/api/docs'
API_URL = 'http://localhost/v2/swagger.json'  # Our API url (can of course be a local resource)


# --------------------------------------------------------view----------------------------------------------------------
@app.route("/")
@app.route("/hello")
def hello_world():
    return "hello_world"


# ------------------------------------------------------interface-------------------------------------------------------

@logger.catch()
@ns.route('/v1/app/<string:name>')
class Username(BaseRestful):
    def get(self, name):

        return 'get' + name

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
