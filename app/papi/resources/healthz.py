from papi.config import Config
from flask_restplus import Resource, Namespace

""" init the namespace for these routes """
api = Namespace('/', description='Health check endpoint.')

# configure load balancer healthz
@api.route('/healthz')
class Healthz(Resource):
    @api.doc("Load balancer healthz checks without any other integration testing.")
    def get(self):
        return {
            'microservice': 'pets-api',
            'verion': Config.VERSION
        }