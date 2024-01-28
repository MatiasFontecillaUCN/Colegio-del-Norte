from models.models import EnrollmentApplications
from models.models import Users
from models.models import Students
from models.models import Classes
from models.models import ClassesStudents
from models.models import Administrators
from app.schemas.EnrollmentApplicationSchema import EnrollmentApplicationSchema
from app.controllers.StudentController import StudentController
from app.controllers.UserController import UserController
from Helpers.ValidationHelpers import ValidationHelpers
from flask import jsonify
import random
import datetime

class EnrollmentController:
    def edit_enrollment(enrollment_id,status):
        try:
            enrollment = EnrollmentApplications.execute_query(id=enrollment_id)
            user_rut = enrollment.user_rut
            student_rut = enrollment.student_rut
            find_user = Users.execute_query(rut=user_rut)
            find_student = Students.execute_query(rut=student_rut)
            find_user.status = status
            find_student.status = status
            find_user.update()
            find_student.update()
            enrollment.status = status
            enrollment.update()
            if(status == 1):
                EnrollmentController.create_classes(find_student)
            return True
        except Exception as e:
            print("Error:", e)
            return False
    
    def create_classes(student):
        year_student = student.school_year
        classes = Classes.execute_query_all(school_year=year_student)
        for obj_class in classes:
            new_class_student = ClassesStudents(
                    class_id=obj_class.id,
                    student_rut=student.rut,
                    grade=random.randint(10, 70),
                )
            new_class_student.insert()

    def create_enrollmentAplication_user_student(user_rut, user_name, user_lastname, user_phone_number, user_email, student_rut, student_name, student_lastname, student_school_year, student_parallel, student_email, student_phone_number, administrator_rut):
        
        if(UserController.validate_user(user_rut, user_name, user_lastname, user_phone_number, user_email)):
            if(StudentController.validate_student(student_rut, student_name, student_lastname, student_school_year, student_parallel, student_email, student_phone_number, user_rut)):
                return EnrollmentController.create_enrollmentApplication(user_rut, user_name, user_lastname, user_phone_number, user_email, student_rut, student_name, student_lastname, student_school_year, student_parallel, student_email, student_phone_number, administrator_rut)
            else:
                return jsonify({'Error': 'Error al crear estudiante','created':False})
        else:
            return jsonify({'Error': 'Error al crear usuario','created':False})

    def create_enrollmentApplication(user_rut, user_name, user_lastname, user_phone_number, user_email, student_rut, student_name, student_lastname, student_school_year, student_parallel, student_email, student_phone_number, administrator_rut):
        try:
            user_rut = ValidationHelpers.validate_rut(user_rut)
            administrator_rut = ValidationHelpers.validate_rut(administrator_rut)
            student_rut = ValidationHelpers.validate_rut(student_rut)
            user = Users.execute_query(rut=user_rut)
            administrator = Administrators.execute_query(rut=administrator_rut)
            if(administrator == False):
                return jsonify({'Error': 'No se creo la solicitud de matricula, administrador no encontrado','created':False})
            if(user==False):
                user = Users(
                    password=user_rut.replace('.','').replace('-',''),
                    rut=user_rut,
                    name=user_name,
                    lastname=user_lastname,
                    email=user_email,
                    phone_number=user_phone_number,
                    status=2
                )
                user.insert()
            else:
                enrollments = EnrollmentApplications.execute_query_all(user_rut=user.rut)
                count = 0
                for enrollment in enrollments:
                    count += 1
                if(count >= 5):
                    return jsonify({'Error': 'No se creo la solicitud de matricula, el apoderado tiene 5 o mas matriculas','created':False})

            new_student = Students(
                rut=student_rut,
                name=student_name,
                lastname=student_lastname,
                school_year=student_school_year,
                parallel_name=student_parallel,
                email=student_email,
                phone_number=student_phone_number,
                status=2,
                attendance=float(random.randint(70,100)/100),
                user_rut=user.rut
            )
            new_student.insert()

            new_enrollment = EnrollmentApplications(
                date=datetime.date.today(),
                user_rut=user.rut,
                student_rut=new_student.rut,
                administrator_rut=administrator.rut,
                status=2
            )
            new_enrollment.insert()
            enrollment_schema = EnrollmentApplicationSchema()
            enrollment_json = enrollment_schema.dump(new_enrollment)
            return jsonify({'message': 'Solicitud de matricula creada correctamente', 'enrollment': enrollment_json,'created':True})
        except Exception as e:
            print(e)
            return jsonify({'Error': 'No se creo la solicitud de matricula','created':False})

    def get_enrollments_user(user_rut):
        user_rut = ValidationHelpers.validate_rut(user_rut)
        enrollments = EnrollmentApplications.execute_query_all(user_rut=user_rut)
        json_enrollments = {'enrollments':[]}
        for enrollment in enrollments:
            date = str(enrollment.date)[:10].split(' ')[0]
            student_rut = enrollment.student_rut
            student = Students.execute_query(rut=student_rut)
            student_name = student.name + " " + student.lastname
            year_parallel = ""
            status = ""

            if(student.school_year < 8):
                year_parallel = str(student.school_year) + " básico " + student.parallel_name
            else:
                year_parallel = str(student.school_year - 8) + " medio " + student.parallel_name

            json_enrollments['enrollments'].append({'id':enrollment.id,'date':date,'student_name':student_name,'year_parallel':year_parallel,'status':enrollment.status})
        return jsonify(json_enrollments)

    def get_enrollments():
        enrollments = EnrollmentApplications.execute_query_all(status=2)
        json_enrollments = {'enrollments':[]}
        for enrollment in enrollments:
            date = str(enrollment.date)[:10].split(' ')[0]
            student_rut = enrollment.student_rut
            user_rut = enrollment.user_rut
            student = Students.execute_query(rut=student_rut)
            user = Users.execute_query(rut=user_rut)
            student_name = student.name + " " + student.lastname
            year_parallel = ""
            user_name = user.name + " " + user.lastname
            if(student.school_year <= 8):
                year_parallel = str(student.school_year) + " básico " + student.parallel_name
            else:
                year_parallel = str(student.school_year - 8) + " medio " + student.parallel_name

            json_enrollments['enrollments'].append({'id':enrollment.id,'date':date,'user_name':user_name,'student_name':student_name,'year_parallel':year_parallel})
        return jsonify(json_enrollments)


