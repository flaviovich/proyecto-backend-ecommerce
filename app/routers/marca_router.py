from app import app
from flask import request
from app.controllers.marca_controller import MarcaController

@app.route("/marcas", methods=['GET'])
def listar():  # sourcery skip: inline-immediately-returned-variable
    marcas = MarcaController().getAll()
    return marcas

@app.route("/marca", methods=['POST'])
def crear():  # sourcery skip: inline-immediately-returned-variable
    json_input = request.get_json()
    result = MarcaController().post(json_input)
    return result

@app.route("/marca/<int:id>", methods=['PUT'])
def actualizar(id):
    marca = MarcaController()
    json_input = request.get_json()
    return marca.update(id, json_input)

@app.route("/celular/<int:id>", methods=['DELETE'])
def eliminar(id):
    marca = MarcaController()
    return marca.delete(id)
