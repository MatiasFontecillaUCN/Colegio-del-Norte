from flask import request
from app.controllers.ProfessorController import ProfessorController
from flask_jwt_extended import jwt_required
from flask_jwt_extended import verify_jwt_in_request



def add_professor_routes(app):

    @app.route('/professors', methods=['GET', 'POST', 'PATCH', 'DELETE'])
    def get_professors():
        if request.method == 'PATCH':
            verify_jwt_in_request()
            data = request.get_json()
            return ProfessorController.edit_professor(data.get('name'),data.get('lastname'),data.get('rut'),data.get('phone_number'),data.get('email'),data.get('subject'))
            
        elif request.method == 'DELETE':
            verify_jwt_in_request()
            data = request.get_json()
            return ProfessorController.delete_professor(data.get('rut'))
        
        elif request.method == 'POST':
            verify_jwt_in_request()
            data = request.get_json()
            return ProfessorController.create_professor(data.get('name'),data.get('lastname'),data.get('rut'),data.get('phone_number'),data.get('email'),data.get('subject'))
        elif request.method == 'GET':
            return ProfessorController.get_professors()