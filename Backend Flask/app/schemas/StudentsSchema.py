from marshmallow import fields
from app.ext import ma

class StudentsSchema(ma.Schema):
    rut = fields.String(dump_only=True)
    name = fields.String()
    lastname = fields.String()
    school_year = fields.Integer()
    parallel_name = fields.String()
    attendance = fields.Float()
    status = fields.Integer()
    email = fields.String()
    phone_number = fields.String()
    user_rut = fields.String()