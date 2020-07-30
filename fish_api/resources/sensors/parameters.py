from marshmallow import Schema, fields


class SensorSchema(Schema):
    id = fields.Str(required=False)
    name = fields.Str(required=False)
    type = fields.List(fields.Str())
    description = fields.Str(required=False)


class SensorDataSchema(Schema):
    id = fields.Str(required=False)
    sensor = fields.Str(required=False)
    value = fields.Str(required=False)
    unit = fields.Str(required=False)

