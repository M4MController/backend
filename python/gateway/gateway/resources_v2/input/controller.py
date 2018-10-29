from marshmallow import Schema, fields

class ControllerCreateSchema(Schema):
    mac = fields.String()
    controller_type = fields.Integer()

class ControllerActivateSchema(Schema):
    name = fields.String()
    meta = fields.String()
    object_id = fields.Integer()

controller_create_schema = ControllerCreateSchema()
controller_activate_schema = ControllerActivateSchema()
