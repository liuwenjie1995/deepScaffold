import click
from tools.app_path import app
from tools.projectlog import logger
from router_view.main_view import mainpages
# from router_restplus.rest_template import api_v1
from router_restplus.background_change_api import api_v1
from db.sqlorm import get_session, init_db, Base, engine
from flask_cors import CORS

logger.info('----------------------------------------start db_conn----------------------------------------------------')
Base.metadata.create_all(engine)
session = get_session()
init_db()
CORS(app, supports_credentials=True)

@click.command()
@click.option("--port", default=8080)
@click.option("--host", default="0.0.0.0", type=str)
@click.option("--debug", default=True, type=bool)
def run(port, host, debug):
    app.run(port=port, host=host, debug=debug)


logger.info('------------------------------------------view-------------------------------------------------------')
app.register_blueprint(mainpages, url_prefix='/')
logger.info('----------------------------------------interface----------------------------------------------------')
app.register_blueprint(api_v1)


if __name__ == '__main__':
    run()
