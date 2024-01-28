from flask import request,jsonify
from app.controllers.AuthController import AuthController

def add_auth_routes(app):

    @app.route('/login', methods=['POST'])
    def login():
        rut = request.form['rut']
        password = request.form['password']
        return AuthController.login(rut, password)