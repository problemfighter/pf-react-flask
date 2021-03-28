import os


class BaseConfiguration(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SECRET_KEY = 'random_secret_key_base'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/pf_react_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_PATH = "./static/bl-uploads"
