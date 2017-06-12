import configparser
from sqlalchemy import create_engine
def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    config = configparser.ConfigParser()
    config.read('database.ini')
    return create_engine(config.get('DB','sqlalchemy.url'))