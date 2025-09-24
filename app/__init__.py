from flask import Flask
from flask_restx import Api
from .config import Config
from .extensions import db
from .controllers.user_controller import api as user_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)

    # RESTX API
    api = Api(app, version="1.0", title="User API",
              description="A simple Flask-RESTX API")
    api.add_namespace(user_ns, path="/users")

    return app
