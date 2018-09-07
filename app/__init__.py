from flask import Flask
from config import DevConfig

def create_app(config_name):
    # Intializing application
    app = Flask(__name__)


    # Setting up configuration
    app.config.from_object(DevConfig)
    app.config.from_object(config_options[config_name])




     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app