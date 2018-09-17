import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://yego:pass123@localhost/blog'
    SECRET_KEY=os.environ.get('SECRET_KEY') or '1234'
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    SECRET_KEY=os.environ.get('SECRET_KEY')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True    
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