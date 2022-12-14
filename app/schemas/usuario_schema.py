from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario

class UsuarioSchema(Schema):
    usuario_id = fields.Integer(dump_only=True)
    nombres = fields.String(required=True, validate=campo_necesario)
    apellidos = fields.String(required=True, validate=campo_necesario)
    direccion = fields.String()
    email = fields.String(required=True, validate=campo_necesario)
    password = fields.String(required=True, load_only=True, validate=campo_necesario)
    estado = fields.Boolean(dump_only=True)
    created_at = fields.DateTime(load_only=True)
    updated_at = fields.DateTime(load_only=True)

class AutenticacionSchema(Schema):
    password =  fields.String(required=True, validate=campo_necesario)
    email = fields.String(required=True, validate=campo_necesario)
