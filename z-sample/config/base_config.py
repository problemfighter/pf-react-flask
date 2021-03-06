import os


class BaseConfiguration(object):
    CONFIG_ROOT = os.path.abspath(os.path.dirname(__file__))
    APP_ROOT = os.path.abspath(os.path.dirname(CONFIG_ROOT))
    BASE_ROOT = os.path.abspath(os.path.dirname(APP_ROOT))
    BASE_STATIC = os.path.abspath(os.path.join(BASE_ROOT, "static"))
    TEMP_DIR = os.path.abspath(os.path.join(BASE_ROOT, "tmp"))
    DEBUG = True
    SECRET_KEY = 'random_secret_key_base'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/pf_react_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
