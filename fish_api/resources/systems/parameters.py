from marshmallow import Schema, fields


class SystemSchema(Schema):
    id = fields.Str(required=False)
    name = fields.Str(required=False)
    description = fields.Str(required=False)

