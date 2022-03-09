import sys
from configs.config import config, MODE


def get_logger():
    status_config = config.get(MODE)
    mylogger = status_config.LOGGER
    mylogger.info(sys.stdout, colorize=True, format='<green>{time}</green> <level>{message}</level>')
    return mylogger


logger = get_logger()


