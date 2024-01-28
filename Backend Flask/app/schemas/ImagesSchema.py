"""
Módulo ImagesSchema

Este módulo contiene la definición de la clase ImagesSchema, que se utiliza para serializar y deserializar datos relacionados con imágenes.

"""
from marshmallow import fields
from app.ext import ma

class ImagesSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    description = fields.String()
    url = fields.String()
