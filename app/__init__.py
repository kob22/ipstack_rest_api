from flask import Flask
from config import Config

def create_app(config_class=Config):
    """Creates and return flask app"""

    # new flask app from config
    app = Flask(__name__)
    app.config.from_object(config_class)

    # todo json ENCODER for mongo response?
    # todo logging

    from app.web import bp as web_bp
    app.register_blueprint(web_bp)

    return app
