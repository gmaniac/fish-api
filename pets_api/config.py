import os

class Config:
    try:
        VERSION = os.environ['papi.app.version']
    except KeyError:
        VERSION = "0.1.0"
    # SECRET_KEY = os.environ['papi.app.secret_key']
    SECRET_KEY = '|\x85\xe9\\wb\x81\x1d\xa7T\xa5SCt\xfc\xeb\x8b\xcbRQ\x1e=C\xf7'

