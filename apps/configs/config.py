import os
from loguru import logger

basedir = os.path.abspath(os.path.dirname(__file__))
MODE = "dev"


class BaseConfig:  # 基本配置类
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    ITEMS_PER_PAGE = 10
    LOGGER = logger
    logger_compression = 'zip'


class DevelopmentConfig(BaseConfig):  # 开发环境
    DEBUG = True
    username = 'root'
    psw = "123456"
    ip = "localhost"
    port = "3306"
    dbname = "deep"
# engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
    SQL_URL = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8mb4".format(username, psw, ip, port, dbname)

    logger_retention = '1 days'


class TestingConfig(BaseConfig):  # 测试环境
    TESTING = True
    WTF_CSRF_ENABLED = False
    username = 'root'
    psw = "123456"
    ip = "localhost"
    port = "3306"
    dbname = "deep"
    SQL_URL = "mysql+pymysql:{}:{}@{}:{}/{}?charset=utf8mb4".format(username, psw, ip, port, dbname)
    logger_retention = '1 hours'


class ProductionConfig(BaseConfig):  # 生产环境
    TESTING = True
    WTF_CSRF_ENABLED = False
    username = 'root'
    psw = "123456"
    ip = "localhost"
    port = "3306"
    dbname = "deep"
    SQL_URL = "mysql+pymysql:{}:{}@{}:{}/{}?charset=utf8mb4".format(username, psw, ip, port, dbname)
    logger_retention = '1 days'


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig
}
