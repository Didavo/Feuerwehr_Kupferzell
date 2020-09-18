from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
from config import ProductionConfig
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
    print("die globals sind", globals())


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api/v1')


    # if app.config['SSL_REDIDRECT']:
    #     from flask_sslify import SSLify
    #     sslify = SSLify(app)



    return app
