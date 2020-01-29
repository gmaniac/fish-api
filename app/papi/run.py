import os
from flask_restplus import Api
from papi.bootstrappy import Bootstrappy

# Custom Imports
from .config import Config

bootstrappy = Bootstrappy(Config)
app = bootstrappy.bootstrap()

api = bootstrappy.api(version='0.0.1', title='Pets API', description='Pets API supplies the backend for pets-on-pets.')

# Custom Resources
from .resources.debug import api as debug
from .resources.healthz import api as healthz

# add namespaces here for each controller
api.add_namespace(debug)
api.add_namespace(healthz)

# init restful api
api.init_app(app)

if __name__ == "__main__":
    app.run()