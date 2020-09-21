from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import ProductionConfig, TestingConfig
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()


bootstrap = Bootstrap()


login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # if app.config['SSL_REDIDRECT']:
    #     from flask_sslify import SSLify
    #     sslify = SSLify(app)
    return app

