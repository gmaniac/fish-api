from flask import Blueprint, Flask
from flask_restplus import Api
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine


class Bootstrappy(object):

    def __init__(self, config):
        self._config = config
        self._blueprint = None
        self._app = None
        self._api = None
        self._db  = None

    def bootstrap(self):

        self._app = Flask(__name__)
        self._app.config.from_object(self._config)

        # add bcrypt to flask
        flask_bcrypt = Bcrypt()
        flask_bcrypt.init_app(self._app)

        # Create database connection object
        self._db = MongoEngine(self._app)
        
        self._app.app_context().push()
        
        return self._app

    def blueprint(self, url_prefix):

        self._blueprint = Blueprint('api', __name__, url_prefix=url_prefix)

        # register blueprints
        self._app.register_blueprint(self._blueprint)

    def api(self, **kwargs):

        self._api = Api(version=kwargs["version"],
                        title=kwargs["title"],
                        description=kwargs["description"],
                        security=kwargs["security"],
                        authorizations=kwargs["authorizations"])

        return self._api

