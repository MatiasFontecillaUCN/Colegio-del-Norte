from app.controllers.UserController import UserController
from flask import jsonify, request
from flask_jwt_extended import jwt_required

def add_user_routes(app):
    @app.route('/user/<rut>/<name>/<lastname>/<email>/<phone_number>', methods = ['GET'])
    def user_exists(rut, name, lastname, email, phone_number):
        return UserController.user_exists(rut, name, lastname, email, phone_number)
    
    @app.route('/user', methods = ['POST'])
    @jwt_required()
    def create_user():
        data = request.get_json()
        UserController.create_user(data.get('rut'),data.get('name'),data.get('lastname'),data.get('email'),data.get('phone_number'))
        return jsonify({"message":"Usuario creado exitosamente"})
    
    @app.route('/user/<rut>', methods=['GET'])
    def get_user(rut):
        return UserController.get_user(rut)