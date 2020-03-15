from pets_api.bootstrappy import Bootstrappy

from pets_api.resources.healthz import api as healthz_namespace
from pets_api.resources.users import api as user_namespace

# Custom Imports
from pets_api.config import Config

authorizations = {
    'Basic Auth': {
        'type': 'basic',
        'in': 'header',
        'name': 'Authorization'
    },
}

bootstrappy = Bootstrappy(Config)
app = bootstrappy.bootstrap()
# bootstrappy.blueprint(url_prefix='/api/v1')

api = bootstrappy.api(version=Config.VERSION,
                      title='Pets API',
                      description='Pets API supplies the backend for pets-on-pets.',
                      security='Basic Auth',
                      authorizations=authorizations)

# Health check/status
api.add_namespace(healthz_namespace)

# User(s)
api.add_namespace(user_namespace)

