from flask_cors import CORS

from fish_api.bootstrappy import Bootstrappy

from fish_api.resources.healthz import api as health_namespace

from fish_api.resources.sensors.sensors import api as sensors_namespace
from fish_api.resources.sensors.sensor_data import api as sensor_data_namespace

# Custom Imports
from fish_api.config import Config

bootstrappy = Bootstrappy(Config)

app = bootstrappy.bootstrap()
CORS(app)

from fish_api.db import db

# Initiate db connection
db.init_app(app)

api = bootstrappy.api(version=Config.VERSION,
                      title='Fish API',
                      description='Fish API supplies the backend for sending and receiving sensor data.')

# health check
api.add_namespace(health_namespace)

# Sensors
api.add_namespace(sensors_namespace)
api.add_namespace(sensor_data_namespace)

