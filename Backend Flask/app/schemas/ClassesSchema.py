from marshmallow import fields
from app.ext import ma

class ClassesSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    subject = fields.String()
    school_year = fields.Integer()
    professor_rut = fields.String()