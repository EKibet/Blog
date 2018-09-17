from flask import Flask
from config import config_options,Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
boostrap =Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

'''
The auth.login is the function(or endpoint) name for the login views
'''
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)
    db.init_app(app)

    boostrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
