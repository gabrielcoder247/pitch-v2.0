from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options

# Instantiating extensions
db = SQLAlchemy()

def create_app(config_name):
    # Intializing application
    app = Flask(__name__)


     # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)



     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')



    return app