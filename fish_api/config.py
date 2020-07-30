import os


class Config:
    # set default values when not available
    VERSION = os.environ.get('fish.app.version', "0.1.0")
    MONGODB_SETTINGS = {
        'db': 'sensors',
        'port': 27017,
        'host': '127.0.0.1'
    }

