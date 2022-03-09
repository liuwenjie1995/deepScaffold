import sys
import os

root_path = '../../docs'
from configs.config import config, MODE


def get_logger():
    status_config = config.get(MODE)
    _logger = status_config.LOGGER
    _logger.add(status_config.LOG_PATH,
                format=status_config.logger_format,
                rotation=status_config.logger_rotation,
                retention=status_config.logger_retention,
                compression=status_config.logger_compression,
                level=status_config.logger_level
                )
    return _logger


logger = get_logger()
