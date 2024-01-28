from marshmallow import fields
from app.ext import ma

class UsersSchema(ma.Schema):
    rut = fields.String(required=True)
    name = fields.String(required=True)
    lastname = fields.String(required=True)
    password = fields.String(required=True)
    status = fields.Integer(required=True)
    email = fields.String(required=True)
    phone_number = fields.String(required=True)