from config.base_config import BaseConfiguration


class ProdConfiguration(BaseConfiguration):
    SECRET_KEY = 'random_secret_key_prod'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/pf_react_flask'
