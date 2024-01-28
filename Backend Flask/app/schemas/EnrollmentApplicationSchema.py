from marshmallow import fields
from app.ext import ma

class EnrollmentApplicationSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    date = fields.Date()
    status = fields.Integer()
    user_rut = fields.String()
    student_rut = fields.String()
    administrator_rut = fields.String()