"""
Módulo AdministratorsSchema

Este módulo contiene la definición de la clase AdministratorsSchema, que se utiliza para serializar y deserializar datos relacionados con administradores.

"""
from marshmallow import fields
from app.ext import ma


class AdministratorsSchema(ma.Schema):
    rut = fields.String(dump_only=True)
    password = fields.String()
