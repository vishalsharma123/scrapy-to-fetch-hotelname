from sqlalchemy import create_engine, Column, Integer, Float ,String, DateTime,JSON,Boolean,Text , Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.sql import func
from bookinghotel.settings import *
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
import configparser
import os

from sqlalchemy.engine.url import URL
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float ,String, DateTime,JSON
from sqlalchemy.orm import sessionmaker
import configparser
#
# W73TransferDeclarativeBase = declarative_base()
#
#
# def adapt_numpy_int64(numpy_int64):
#     """Integer type cast for Pandas."""
#     return AsIs(numpy_int64)
#
# register_adapter(np.int64, adapt_numpy_int64)
#
#
# def addapt_numpy_bool(numpy_bool):
#     """Boolean type cast for Pandas."""
#     return AsIs(numpy_bool)
#
# register_adapter(np.bool_, addapt_numpy_bool)
#
#
#
#
# def create_W73Transfer_table(engine):
#     W73TransferDeclarativeBase.metadata.create_all(engine)
#
#
# class W73Transfer (W73TransferDeclarativeBase):
#     __tablename__ = "W73Transfer_table"
#
#     id = Column(Integer, primary_key=True)
#     hotellist_inner = Column('hotellist_inner',String(3000),nullable=True)


from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL




DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    config = configparser.ConfigParser()
    config.read('database.ini')
    return create_engine(config.get('DB','sqlalchemy.url'))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)

    hotel_name= Column('hotel_name', String)
    time_booked = Column('time_booked', String)
    strike_through_price =  Column('strike_through_price', String)
    discount_price = Column('discount_price', String)
    available_rooms = Column('available_rooms', String)
    address = Column('address', String)







