import os
from app import create_app
from flask_jwt_extended import create_access_token
import pytest
from models.models import Administrators
import pytest
from models.models import *
import datetime
import random

def generate_random_rut():
        return str(random.randint(10000000, 99999999))+ str(random.randint(0, 9))

@pytest.fixture(scope='session')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!

    

@pytest.fixture(scope='session')
def create_adm():
    adm = Administrators(rut=generate_random_rut(),password='niño123')
    adm.insert()
    yield adm

@pytest.fixture(scope='session')
def create_token_adm(create_adm):
    addtional_claims = {"roles":"user"}
    access_token_admin = create_access_token(identity=create_adm.rut,additional_claims=addtional_claims)
    return access_token_admin

@pytest.fixture(scope='session')
def create_user():
    user = Users(rut=generate_random_rut(),name="Pedro",lastname="Pascal",password="password",status=2,email="example@gmail.com",phone_number="54255665")
    user.insert()
    yield user


@pytest.fixture(scope='session')
def create_token_user(create_user):
    addtional_claims = {"roles":"user"}
    access_token_admin = create_access_token(identity=create_user.rut,additional_claims=addtional_claims)
    return access_token_admin


@pytest.fixture(scope='session')
def create_student(create_user, test_client):
    school_year = random.randint(0,12)
    response = test_client.get(f'/student-year-spots/{school_year}')
    data = response.get_json()
    spots = data['cupos']
    parallel = data['parallel']
    user = create_user
    student = Students(rut=generate_random_rut(),name="Jose",lastname="Gallardo",school_year=school_year,parallel_name=parallel,attendance=0.5,status=2,user_rut=user.rut,email="example@gmail.com",phone_number="56482335")
    student.insert()
    yield student

@pytest.fixture(scope='session')
def create_enrollment(create_adm,create_user,create_student):
    user = create_user
    adm = create_adm
    student = create_student
    enrollment = EnrollmentApplications(date=datetime.date.today(),user_rut=user.rut,student_rut=student.rut,administrator_rut=adm.rut,status=2)
    enrollment.insert()
    yield enrollment


@pytest.fixture(scope='session')
def create_student_2(create_user):
    user = create_user
    student = Students(rut=generate_random_rut(),name="Juan",lastname="Busch",school_year=10,parallel_name="B",attendance=0.7,status=2,user_rut=user.rut,email="examplee@gmail.com",phone_number="56482345")
    student.insert()
    yield student

@pytest.fixture(scope='session')
def create_enrollment_2(create_adm,create_student_2,create_user):
    user = create_user
    adm = create_adm
    student = create_student_2
    enrollment = EnrollmentApplications(date=datetime.date.today(),user_rut=user.rut,student_rut=student.rut,administrator_rut=adm.rut,status=2)
    enrollment.insert()
    yield enrollment


@pytest.fixture(scope='session')
def create_professor():
    professor = Professors(rut=generate_random_rut(), name='John', lastname='Doe', phone_number='123456789', email='john.doe@example.com', subject='Mathematics', status=1)
    professor.insert()
    yield professor