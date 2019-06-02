from marshmallow import Schema, fields


class CompanyCreateSchema(Schema):
    name = fields.String()
    phone = fields.String()
    address = fields.String()

copany_create_schema = CompanyCreateSchema()
