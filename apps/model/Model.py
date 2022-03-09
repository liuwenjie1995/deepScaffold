from abc import ABCMeta
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import UniqueConstraint, Index
from sqlalchemy import Integer, String, ForeignKey, BOOLEAN

from db.sqlorm import engine
from tools.projectlog import logger
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, ValidationError, constr
from typing import Optional
Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


@logger.catch()
def get_session():
    Session = sessionmaker(bind=engine)
    session = Session
    return session
