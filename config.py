import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yego:pass123@localhost/blog'

    SECRET_KEY=os.environ.get('SECRET_KEY')
    pass
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yego:pass123@localhost/blog'
    DEBUG = True
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yego:pass123@localhost/blog'
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}