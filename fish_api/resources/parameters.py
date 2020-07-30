from marshmallow import Schema, fields


class PaginationSchema(Schema):
    kwords = fields.Dict(required=False)
    page = fields.Int(required=False, missing=1)
    count = fields.Int(required=False, missing=10)

