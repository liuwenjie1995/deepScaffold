import click
from sqlalchemy import create_engine
from configs.config import *
from tools.projectlog import get_logger
config = config.get(MODE)

engine = create_engine(
    config.SQL_URL, echo=True, max_overflow=5
)


