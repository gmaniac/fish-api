from flask_restplus import Namespace, Resource

# Custom Imports

api = Namespace('developer', description='Debugger Resource')

"""
 Class Resource to handle debugging
"""


@api.route('/debug')
class Debug(Resource):
    
    @api.doc('GET:: developer debug')
    def get(self):
        return {"data": "developer mode enabled"}