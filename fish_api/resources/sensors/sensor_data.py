from flask_restplus import abort, Resource, Namespace, fields
from webargs.flaskparser import use_args

from .parameters import SensorDataSchema
from fish_api.resources.parameters import PaginationSchema
from fish_api.resources.sensors.sensors import sensor_model

from fish_api.daos.sensor_data import SensorDataDAO

""" init the namespace for these routes """
api = Namespace('/')


sensor_data_model = api.model('SensorData', {
    'id': fields.String(required=True, description='user identifier'),
    'sensor': fields.Nested(sensor_model, required=False, description='sensor associated to'),
    'value': fields.String(required=False, description='sensor data value'),
    'unit': fields.String(required=False, description='sensor data unit'),
    'date_created': fields.DateTime(required=True, description='date user created')
})


@api.route('/sensors-data')
class SensorsData(Resource):
    """
    Sensors Data Resource
    """

    @api.doc('GET - Sensor data list')
    @use_args(PaginationSchema, locations=['query'])
    @api.marshal_with(sensor_data_model, as_list=True)
    def get(self, args):
        return list(SensorDataDAO.get_all(sensor=args['sensor'], page=args['page'], count=args['count']))

    @api.doc('DELETE - user(s)')
    @use_args(SensorDataSchema)
    def delete(self, args):
        return SensorDataDAO.delete(args)

    @api.doc('POST - system(s)')
    @use_args(SensorDataSchema)
    def post(self, args):
        return SensorDataDAO.create(args)


@api.route('/sensor-data/<string:id>')
@api.param('id', 'The sensor data identifier')
class SensorDataById(Resource):
    """
    Sensor Data Resource
    """

    @api.doc('GET - sensor data')
    @api.marshal_with(sensor_data_model)
    @api.response(404, 'Sensor data not found')
    def get(self, id):
        sensor_data = SensorDataDAO.get({'id': id})

        if sensor_data is None:
            abort(404, "Sensor data not found")

        return sensor_data

    @api.doc('PUT - sensor data')
    @use_args(SensorDataSchema)
    @api.marshal_with(sensor_data_model)
    @api.response(404, 'Sensor data not found')
    def put(self, args, username):
        return SensorDataDAO.update(username, args)

