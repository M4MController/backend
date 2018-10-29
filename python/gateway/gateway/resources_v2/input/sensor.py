from marshmallow import Schema, fields

class SensorCreateSchema(Schema):
    sensor_type = fields.Integer()
    name        = fields.String()
    company     = fields.String()
    controller_id=fields.Integer()

sensor_create_schema = SensorCreateSchema()
