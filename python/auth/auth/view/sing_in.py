from marshmallow import Schema, fields, post_load

class SignInSchema(Schema):
    e_mail = fields.String()
    password = fields.String()

    @post_load
    def strip_e_mail(self, item):
        item['e_mail'] = item['e_mail'].strip()
        return item


sign_in_schema = SignInSchema()
