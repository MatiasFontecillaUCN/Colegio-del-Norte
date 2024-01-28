from flask import jsonify, request
from app.controllers.EnrollmentController import EnrollmentController
from flask_jwt_extended import jwt_required
from flask_jwt_extended import verify_jwt_in_request


def add_enrollment_routes(app):

    @app.route('/enrollment', methods=['POST','PATCH','GET'])
    def get_enrollments():
        if request.method == 'PATCH':
            verify_jwt_in_request()
            data = request.get_json()
            if EnrollmentController.edit_enrollment(data.get('enrollment_id'),data.get('status')):
                return jsonify({'message': 'Matricula editada correctamente', 'edited':True})
            else:
                return jsonify({'message': 'Error al editar matricula', 'edited':False})
        
        elif request.method == 'POST':
            data = request.get_json()
            return EnrollmentController.create_enrollmentAplication_user_student(data.get('user_rut'),data.get('user_name'),data.get('user_lastname'),data.get('user_phone_number'),data.get('user_email'),data.get('student_rut'),data.get('student_name'),data.get('student_lastname'),data.get('student_school_year'),data.get('student_parallel'),data.get('student_email'),data.get('student_phone_number'),data.get('administrator_rut'))
        
        elif request.method == 'GET':
            verify_jwt_in_request()
            return EnrollmentController.get_enrollments()
        
    @app.route("/enrollment-user/<rut>")
    @jwt_required()
    def get_enrolments_user(rut):
        return EnrollmentController.get_enrollments_user(rut)
        