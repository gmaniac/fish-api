import os

class Config:
    # set default values when not available
    VERSION = os.environ.get('papi.app.version', "0.1.0")
    SECRET_KEY = os.environ.get('papi.app.secret_key', '|\x85\xe9\\wb\x81\x1d\xa7T\xa5SCt\xfc\xeb\x8b\xcbRQ\x1e=C\xf7')

