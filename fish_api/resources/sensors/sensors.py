from flask_restplus import abort, Resource, Namespace, fields
from webargs.flaskparser import use_args

from .parameters import SensorSchema
from fish_api.resources.parameters import PaginationSchema
from fish_api.resources.systems.systems import system_model

from fish_api.daos.sensor import SensorDAO

""" init the namespace for these routes """
api = Namespace('/')


sensor_model = api.model('Sensor', {
    'id': fields.String(required=True, description='sensor identifier'),
    'name': fields.String(required=False, description='name of sensor'),
    'type': fields.List(fields.String(required=False, description='sensor type')),
    'system': fields.Nested(system_model, required=False, description='system associated to'),
    'description': fields.String(required=False, description='description of sensor'),
    'date_created': fields.DateTime(required=True, description='date sensor created')
})


@api.route('/sensors')
class Sensors(Resource):
    """
    Sensors Resource
    """

    @api.doc('GET - sensors list')
    @use_args(PaginationSchema, locations=['query'])
    @api.marshal_with(sensor_model, as_list=True)
    def get(self, args):
        return list(SensorDAO.get_all(page=args['page'], count=args['count']))

    @api.doc('DELETE - sensor(s)')
    @use_args(SensorSchema)
    @api.response(411, 'Length Required')
    def delete(self, args):
        return SensorDAO.delete(args)

    @api.doc('POST - sensor(s)')
    @use_args(SensorSchema)
    def post(self, args):
        return SensorDAO.create(args)


@api.route('/sensors/<string:id>')
@api.param('id', 'The sensor identifier')
class SensorById(Resource):
    """
    Sensor Resource
    """

    @api.doc('GET - sensor')
    @api.marshal_with(sensor_model)
    @api.response(404, 'Sensor not found')
    def get(self, id):
        sensor = SensorDAO.get({'id': id})

        if sensor is None:
            abort(404, "Sensor not found")

        return sensor

    @api.doc('PUT - sensor')
    @use_args(SensorSchema)
    @api.marshal_with(sensor_model)
    @api.response(404, "Sensor not found")
    @api.response(411, "Length required")
    def put(self, args, id):
        return SensorDAO.update(id, args)

