from flask import Flask
from config import config_options,Config
from flask_bootstrap import Bootstrap

boostrap =Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config.from_object(Config)

    boostrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
