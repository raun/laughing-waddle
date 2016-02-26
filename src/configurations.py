# __author__ = 'shanshul'


import os


class Base(object):
    DEBUG = False
    TESTING = False

    MONGODB_DB = 'ticketting_db'


class Production(Base):
    DEBUG = False
    TESTING = False

    MONGODB_SETTINGS = {
        'DB':'ticketting_db',
        'HOST': 'localhost'
        }


class Development(Base):
    DEBUG = True
    TESTING = False


class Testing(Development):
    TESTING = True