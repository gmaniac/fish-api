from flask_restplus import abort, Resource, Namespace, fields
from webargs.flaskparser import use_args

from fish_api.resources.systems.parameters import SystemSchema
from fish_api.resources.parameters import PaginationSchema

from fish_api.daos.system import SystemDAO

""" init the namespace for these routes """
api = Namespace('/')


system_model = api.model('System', {
    'id': fields.String(required=True, description='system identifier'),
    'name': fields.String(required=False, description='name of sensor'),
    'description': fields.String(required=False, description='description of sensor'),
    'date_created': fields.DateTime(required=True, description='date user created')
})


@api.route('/systems')
class Systems(Resource):
    """
    Systems Resource
    """

    @api.doc('GET - System list')
    @use_args(PaginationSchema, locations=['query'])
    @api.marshal_with(system_model, as_list=True)
    def get(self, args):
        return list(SystemDAO.get_all(page=args['page'], count=args['count']))

    @api.doc('DELETE - system(s)')
    @use_args(SystemSchema)
    @api.response(411, 'Length Required')
    def delete(self, args):
        return SystemDAO.delete(args)

    @api.doc('POST - System(s)')
    @use_args(SystemSchema)
    def post(self, args):
        return SystemDAO.create(args)


@api.route('/systems/<string:id>')
@api.param('id', 'The system identifier')
class SystemById(Resource):
    """
    System Resource
    """

    @api.doc('GET - system')
    @api.marshal_with(system_model)
    @api.response(404, 'System not found')
    def get(self, id):
        system = SystemDAO.get({'id': id})

        if system is None:
            abort(404, "User not found")

        return system

    @api.doc('PUT - system')
    @use_args(SystemSchema)
    @api.marshal_with(system_model)
    @api.response(404, 'System not found')
    def put(self, args, id):
        return SystemDAO.update(id, args)

