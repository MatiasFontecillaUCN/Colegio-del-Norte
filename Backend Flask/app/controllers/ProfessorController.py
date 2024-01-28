from app.schemas.ProfessorsSchema import ProfessorsSchema
from Helpers.ValidationHelpers import ValidationHelpers
from models.models import Professors
from flask import jsonify

class ProfessorController:
    
    def get_professors():
        professors = Professors.execute_query_all(status=1)
        if not professors:
           return jsonify({"error":"no hay profesores en la base de datos"})
        professors_schema = ProfessorsSchema(many=True)
        professors = professors_schema.dump(professors)
        return professors    
    def edit_professor(name, lastname, rut, phone_number, email, subject):
        try:
            rut = ValidationHelpers.validate_rut(rut)
            professor = Professors.execute_query(rut=rut)
            professor.name = name
            professor.lastname = lastname
            professor.phone_number = phone_number
            professor.email = email
            professor.subject = subject
            professor.update()
            professors_schema = ProfessorsSchema()
            professors_json = professors_schema.dump(professor)
            return jsonify({'message': 'Profesor editado correctamente', 'professor': professors_json,'edited':True})
        except Exception as e:
            return jsonify({'message': 'Error al editar profesor', 'Error': e,'edited':False})
        
    def delete_professor(rut):
        try:
            rut = ValidationHelpers.validate_rut(rut)
            professor = Professors.execute_query(rut=rut)
            professor.status = 0
            professor.update()
            return jsonify({'message': 'Profesor eliminado correctamente', 'deleted':True})
        except Exception as e:
            return jsonify({'message': 'Error al eliminar el profesor', 'Error': e,'deleted':False})
        
    def create_professor(name, lastname, rut, phone_number, email, subject):
        try:
            rut = ValidationHelpers.validate_rut(rut)
            professor = Professors.execute_query(rut=rut)
            if professor:
                professor.status = 1
                professor.update()
                professors_schema = ProfessorsSchema()
                professors_json = professors_schema.dump(professor)
                return jsonify({'message': 'Profesor creado correctamente', 'professor': professors_json,'created':True})
            professor = Professors(name=name, lastname=lastname, rut=rut, phone_number=phone_number, email=email, subject=subject, status=1)
            professor.insert()
            professors_schema = ProfessorsSchema()
            professors_json = professors_schema.dump(professor)
            return jsonify({'message': 'Profesor creado correctamente', 'professor': professors_json,'created':True})
        except Exception as e:
            print(e)
            return jsonify({'message': 'Error al eliminar el profesor', 'Error': e,'created':False})
