import os
import tempfile



class BaseConfig(object):
    VERSION = f'1.0'
    HOST = '0.0.0.0'
    PORT = 5000
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_MASK_SWAGGER = False
    ERROR_404_HELP = False
    TESTING = False


class prodConfig(BaseConfig):
    CONFIG = 'prod'
    DOMAIN = 'https://localhost'

    DB_USER = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_NAME = 'postgres'
    DB_HOST = 'db'
    DB_PORT = '5432'

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class stagingConfig(BaseConfig):
    CONFIG = 'staging'
    DOMAIN = 'https://localhost'

    DB_USER = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_NAME = 'postgres'
    DB_HOST = 'db'
    DB_PORT = '5432'

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class devConfig(BaseConfig):
    CONFIG = 'dev'
    DOMAIN = 'http://localhost'

    DEBUG = True
    ENV = 'development'

    DB_USER = 'postgres'
    DB_PASSWORD = 'postgres'
    DB_NAME = 'postgres'
    DB_HOST = 'db'
    DB_PORT = '5432'

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@db:5432/postgres'


class testConfig(BaseConfig):
    CONFIG = 'test'
    DOMAIN = 'http://localhost'

    ENV = 'production'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{tempfile.mkstemp()[1]}'


configList = {
    'prod': prodConfig(),
    'staging': stagingConfig(),
    'dev': devConfig(),
    'test': testConfig()
}


def getConfig():
    if os.getenv('ENV') in configList:
        return configList[os.getenv('ENV')]
    else:
        print('Wrong environment config value')
        exit()
