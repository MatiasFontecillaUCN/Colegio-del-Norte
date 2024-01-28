from flask import jsonify, request
from app.controllers.StudentController import StudentController
from flask_jwt_extended import jwt_required

def add_student_routes(app):

    @app.route('/student/<rut>', methods = ['GET'])
    def check_student(rut):
         return StudentController.student_exists(rut)
    
    @app.route('/student-year-spots/<school_year>', methods = ['GET'])
    def check_year_spots(school_year):
        return StudentController.get_parallel_with_spots(school_year)
    
    @app.route('/viewstudents/<user_rut>', methods = ['GET'])
    @jwt_required()
    def view_students(user_rut):
        return StudentController.view_students(user_rut)