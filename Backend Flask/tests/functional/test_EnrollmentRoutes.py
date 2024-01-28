from models.models import EnrollmentApplications
from flask_jwt_extended import decode_token
from models.models import *
import random

def generate_random_rut():
        return str(random.randint(10000000, 99999999))+ str(random.randint(0, 9))

def test_enrollment_post(test_client, create_adm):
    user_rut = generate_random_rut()
    student_rut = generate_random_rut()
    body = {
    "user_rut":user_rut,
    "user_name":"Pedro",
    "user_lastname":"Gonzales",
    "user_phone_number":"99596562",
    "user_email":"p@g.gmail.com",
    "student_rut":student_rut,
    "student_name":"Juan",
    "student_lastname":"Gonzales",
    "student_school_year":"3",
    "student_parallel":"A",
    "student_phone_number":"65354465456",
    "student_email":"asfasf@agas.com",
    "administrator_rut":create_adm.rut
    }
    adm = create_adm
    response = test_client.post('/enrollment', json=body)
    data = response.get_json()
    enrollment = data.get('enrollment')
    db_enrollment = EnrollmentApplications.execute_query(user_rut=enrollment.get('user_rut'),student_rut=enrollment.get('student_rut'))
    db_student = Students.execute_query(rut=enrollment.get('student_rut'))
    db_user = Users.execute_query(rut=enrollment.get('user_rut'))
    assert data.get('created') == True
    assert db_enrollment is not False and db_user is not False and db_student is not False
    assert db_enrollment.status == 2 and db_user.status == 2 and db_student.status == 2

def test_enrollment_get(test_client, create_enrollment, create_token_adm):
    headers = {
    'Authorization': 'Bearer ' + create_token_adm,
    }
    enrollment = create_enrollment
    response = test_client.get('/enrollment', headers=headers)
    data = response.get_json().get('enrollments')
    for enrollment in data:
        assert enrollment.get('id') and enrollment.get('date') and enrollment.get('student_name') and enrollment.get('user_name') and enrollment.get('year_parallel')

def test_enrollment_patch_accept(test_client, create_enrollment, create_token_adm):
    headers = {
    'Authorization': 'Bearer ' + create_token_adm,
    }
    enrollment = create_enrollment
    status = 1
    body = {'enrollment_id':enrollment.id,'status':status}
    response = test_client.patch('/enrollment', json=body, headers=headers)
    data = response.get_json()
    edited = data.get('edited')
    enrollment_db = EnrollmentApplications.execute_query(id=enrollment.id)
    user_db = Users.execute_query(rut=enrollment.user_rut)
    student_db = Students.execute_query(rut=enrollment.student_rut)
    assert edited == True
    assert enrollment_db.status == 1 and student_db.status == 1 and user_db.status == 1

def test_enrollment_user(test_client,create_user,create_token_user):
    user = create_user
    headers = {
    'Authorization': 'Bearer ' + create_token_user,
    }
    response = test_client.get('/enrollment-user/'+user.rut,headers=headers)
    data = response.get_json().get('enrollments')
    for enrollment in data:
        assert EnrollmentApplications.execute_query(id=enrollment.get('id'),user_rut=user.rut) is not False
        


#LOGIN TESTS

def test_login(create_user,test_client):
    user = create_user
    body = {
    "rut": user.rut,
    "password": "password"
    }   
    response = test_client.post('/login', data=body)
    print(response.data)
    token = response.data
    if token is not None:
        decoded_token = decode_token(token)
        assert decoded_token["sub"] == user.rut
    else:
        assert False, "Token is None"

#PROFESSORS TESTS

def test_professors_get(test_client,create_token_adm):
    headers = {
    'Authorization': 'Bearer ' + create_token_adm,
    }
    professors = Professors.execute_all()
    response = test_client.get('/professors',headers=headers)
    data = response.get_json()
    print(data)
    for professor in data:
        assert any(prof.rut == professor.get('rut') for prof in professors)


def test_professors_patch(test_client, create_professor,create_token_adm):
    headers = {
    'Authorization': 'Bearer ' + create_token_adm,
    }
    professor = create_professor
    body = {
        "name": "New Name",
        "lastname": "New Lastname",
        "rut": professor.rut,
        "phone_number": "New Phone Number",
        "email": "new.email@example.com",
        "subject": "New Subject"
    }
    response = test_client.patch('/professors', json=body,headers=headers)
    data = response.get_json().get('professor')
    
    updated_professor = Professors.execute_query(rut=professor.rut)
    assert updated_professor.name == data.get('name')
    assert updated_professor.lastname == data.get('lastname')
    assert updated_professor.phone_number == data.get('phone_number')
    assert updated_professor.email == data.get('email')
    assert updated_professor.subject == data.get('subject')


def test_delete_professor(test_client, create_professor,create_token_adm):
    headers = {
    'Authorization': 'Bearer ' + create_token_adm,
    }
    professor = create_professor
    response = test_client.delete('/professors', json={'rut': professor.rut}, headers=headers)

    deleted_professor = Professors.execute_query(rut=professor.rut)
    assert deleted_professor.status == 0

def test_create_professor(test_client, create_token_adm):
    headers = {
    'Authorization': 'Bearer ' + create_token_adm,
    }
    body = {
        "name": "Test",
        "lastname": "User",
        "rut": generate_random_rut(),
        "phone_number": "1234567890",
        "email": "test@example.com",
        "subject": "Test Subject"
    }
    response = test_client.post('/professors', json=body,headers=headers)
    professor = response.get_json().get('professor')
    print(response.get_json())

    created_professor = Professors.execute_query(rut=professor.get('rut'))
    assert created_professor is not None
    assert created_professor.name == body['name']
    assert created_professor.lastname == body['lastname']
    assert created_professor.phone_number == body['phone_number']
    assert created_professor.email == body['email']
    assert created_professor.subject == body['subject']

#STUDENT TESTS

def test_check_student(test_client, create_student,create_token_user):
    headers = {
    'Authorization': 'Bearer ' + create_token_user,
    }
    student = create_student
    response = test_client.get(f'/student/{student.rut}',headers=headers)
    assert response.get_json().get('exists') == True

def test_check_year_spots(test_client,create_student):
    school_year = create_student.school_year
    response = test_client.get(f'/student-year-spots/{school_year}')
    data = response.get_json()
    spots = data['cupos']
    parallel = data['parallel']
    students= Students.execute_query_all(school_year=school_year,parallel_name=parallel)
    count = 30
    for student in students:
        count -= 1
    assert spots == count
    assert parallel == create_student.parallel_name

def test_view_students(test_client,create_token_user, create_user, create_student,create_student_2):
    headers = {
    'Authorization': 'Bearer ' + create_token_user,
    }
    user = create_user
    response = test_client.get(f'/viewstudents/{user.rut}',headers=headers)
    data = response.get_json()
    students = Students.execute_query_all(user_rut=user.rut)
    print("RESPONSE =")
    print(data[0].get('lastname'))
    for student in data:
        assert any(stud.rut == student.get('rut') for stud in students)
        assert student.get('classes') is not None

#USER TESTS

def test_user_exists(test_client, create_user):
    user = create_user
    response = test_client.get(f'/user/{user.rut}/{user.name}/{user.lastname}/{user.email}/{user.phone_number}')
    assert response.get_json().get('continue') == True


def test_get_user(test_client, create_user):
    user = create_user
    response = test_client.get(f'/user/{user.rut}')
    user_db = Users.execute_query(rut=user.rut)
    data = response.get_json()

    assert data['rut'] == user_db.rut
    assert data['name'] == user_db.name
    assert data['lastname'] == user_db.lastname
    assert data['email'] == user_db.email
    assert data['phone_number'] == user_db.phone_number