import random
from models.models import Students
from models.models import Users
from app.schemas.StudentsSchema import StudentsSchema
from app.schemas.UsersSchema import UsersSchema
from flask import jsonify
import random
from Helpers.ValidationHelpers import ValidationHelpers

from Helpers.ValidationHelpers import ValidationHelpers
from models.models import Classes
from models.models import ClassesStudents
from database.db_mysql import db

class StudentController:    
    def validate_student(rut,name,lastname,school_year,parallel,email,phone_number, user_rut):
        try:
            rut = ValidationHelpers.validate_rut(rut)
            student = Students.execute_query(rut=rut)
            if(student is False):       
                new_student = Students(
                    rut=rut,
                    name=name,
                    lastname=lastname,
                    school_year=school_year,
                    parallel_name=parallel,
                    email=email,
                    phone_number=phone_number,
                    status=0,
                    attendance=float(random.randint(0,100)/100),
                    user_rut=""
                )
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
    

    def student_exists(rut):
        rut = ValidationHelpers.validate_rut(rut)
        student = Students.execute_query(rut=rut)
        if(student):
            return jsonify({"message":"Existe ese estudiante","exists":True})
        return jsonify({"message":"No existe ese estudiante","exists":False})
    
    def get_parallel_with_spots(school_year):
        students = Students.execute_query_all(school_year=school_year)
        if(students == False):
            return jsonify({"message":"No existen estudiantes en ese año","parallel":'A'})
        count_a = 30
        count_b = 30
        count_c = 30
        for student in students:
            if(student.parallel_name == "A"):
                count_a -= 1
            elif(student.parallel_name == "B"):
                count_b -= 1
            elif(student.parallel_name == "C"):
                count_c -= 1
        if(count_a > 0):
            return jsonify({"message":"El paralelo A tiene cupos","cupos":count_a,"parallel":'A'})
        elif(count_b > 0):
            return jsonify({"message":"El paralelo B tiene cupos","cupos":count_b,"parallel":'B'})
        elif(count_c > 0):
            return jsonify({"message":"El paralelo C tiene cupos","cupos":count_c,"parallel":'C'})
        else:
            return jsonify({"Error":'No hay cupos disponibles'})
        

    def view_students(user_rut):
        user_rut = ValidationHelpers.validate_rut(user_rut)
        students = Students.query.filter_by(user_rut=user_rut, status = 1).all()
        if not students:
            return jsonify({'error': 'No se encontraron estudiantes asociados a este RUT'}), 404

        students_data = []
        for student in students:
            # Realizar una consulta que une las tablas ClassesStudents y Classes

            student_classes = db.session.query(
                ClassesStudents.class_id, 
                Classes.subject, 
                Classes.school_year, 
                ClassesStudents.grade
            ).join(Classes, Classes.id == ClassesStudents.class_id).filter(ClassesStudents.student_rut == student.rut).all()

        # Crear una lista de las clases y las notas
            classes_data = [
                {
                    'class_id': class_id, 
                    'subject': subject, 
                    'school_year': school_year,
                    'grade': grade
                } 
                for class_id, subject, school_year, grade in student_classes
            ]

            students_data.append({
                'rut': student.rut,
                'name': student.name,
                'lastname': student.lastname,
                'classes': classes_data
            })

        return jsonify(students_data)
