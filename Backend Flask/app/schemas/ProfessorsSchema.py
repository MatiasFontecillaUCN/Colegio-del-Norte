from marshmallow import fields
from app.ext import ma

class ProfessorsSchema(ma.Schema):
    rut = fields.String(dump_only=True)
    name = fields.String()
    lastname = fields.String()
    phone_number = fields.String()
    email = fields.String()
    subject = fields.String()
    status = fields.Integer()