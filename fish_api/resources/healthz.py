from fish_api.config import Config
from flask_restplus import Resource, Namespace

""" init the namespace for these routes """
api = Namespace('/')


# configure load balancer healthz
@api.route('/healthz')
class Healthz(Resource):
    @api.doc("Load balancer healthz checks without any other integration testing.")
    def get(self):
        return {
            'microservice': 'fish-api',
            'verion': Config.VERSION
        }

