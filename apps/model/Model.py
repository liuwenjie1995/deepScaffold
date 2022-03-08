import this

from db.sqlorm import engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column

from sqlalchemy import Integer, String, ForeignKey, BOOLEAN
from sqlalchemy import UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship

from abc import ABCMeta
from db.sqlorm import engine

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


def get_session():
    Session = sessionmaker(bind=engine)
    session = Session
    return session
