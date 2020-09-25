
# -*- coding: utf-8 -*-
#########################################################
import os


class Config:
    """
    Flask configurations
    """
    ENV = 'development'
    DEBUG = True if int(os.environ['DEBUG']) else False
    # Content Length 50 Mb
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024

    """
    SQLAlchemy configurations
    """
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
        os.environ["MYSQL_USER"],
        os.environ["MYSQL_PASSWORD"],
        os.environ["MYSQL_HOST"],
        os.environ["MYSQL_PORT"],
        os.environ["MYSQL_DATABASE"]
    )

    ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
