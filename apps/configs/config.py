import os
from loguru import logger

basedir = os.path.abspath(os.path.dirname(__file__))
MODE = "dev"


class BaseConfig:  # 基本配置类
    ROOT_PATH = r'C:\\Users\\liu\\PycharmProjects\\deepScaffold'
    LOG_INFO = "runtime"
    LOG_PATH = os.path.join(ROOT_PATH, "docs", '{log_info}.log'.format(log_info=LOG_INFO))
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    ITEMS_PER_PAGE = 10
    LOGGER = logger
    logger_format = "[{time}]|[{level}]<level>{message}</level>"
    logger_level = "INFO"
    logger_compression = 'zip'
    logger_rotation = "1 day"
    logger_retention = '10 day'


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
