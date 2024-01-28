from marshmallow import fields
from app.ext import ma

class ClassesStudentsSchema(ma.Schema):
    class_id = fields.Integer(dump_only=True)
    student_rut = fields.String(dump_only=True)
    grade = fields.Integer()
    