from marshmallow import Schema, fields

class ObjectCreateSchema(Schema):
    name = fields.String()
    address = fields.String()

object_create_schema = ObjectCreateSchema()