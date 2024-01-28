from marshmallow import fields
from app.ext import ma

class AppointmentsSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    date = fields.Date()
    user_rut = fields.String()
    professor_rut = fields.String()