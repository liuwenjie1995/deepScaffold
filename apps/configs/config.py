import os

basedir = os.path.abspath(os.path.dirname(__file__))
MODE = "dev"

class BaseConfig:  # 基本配置类
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    ITEMS_PER_PAGE = 10


class DevelopmentConfig(BaseConfig):  # 开发环境
    DEBUG = True
    username = "root"
    psw = "123"
    ip = "192.168.1.1"
    port = "3306"
    dbname = "mysql"
    SQL_URL = "mysql+pymysql:{}:{}@{}:{}/{}?charset=utf8mb4".format(username, psw, ip, port, dbname)


class TestingConfig(BaseConfig):  # 测试环境
    TESTING = True
    WTF_CSRF_ENABLED = False
    username = "root"
    psw = "123"
    ip = "192.168.1.1"
    port = "3306"
    dbname = "mysql"
    SQL_URL = "mysql+pymysql:{}:{}@{}:{}/{}?charset=utf8mb4".format(username, psw, ip, port, dbname)


class ProductionConfig(BaseConfig):  # 生产环境
    TESTING = True
    WTF_CSRF_ENABLED = False
    username = "root"
    psw = "123"
    ip = "192.168.1.1"
    port = "3306"
    dbname = "mysql"
    SQL_URL = "mysql+pymysql:{}:{}@{}:{}/{}?charset=utf8mb4".format(username, psw, ip, port, dbname)


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig
}
