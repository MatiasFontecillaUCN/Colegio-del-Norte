from flask_seeder import Seeder, Faker, generator
from models.models import *
from flask_bcrypt import Bcrypt
from database.db_mysql import db
import random
import datetime


# All seeders inherit from Seeder
class DemoSeeder(Seeder):

    def generate_random_rut():
        return str(random.randint(10000000, 99999999))+ str(random.randint(0, 9))
    
    def generate_random_phone():
        return "569"+str(random.randint(10000000, 99999999))
    
    def run(self):
        images_about_us = ["Teachers/vdxm042vpjs8ffsrmriz","Teachers/a8ipvqlidaa9jfztna8l","Teachers/jn2ib4ksbzskfp3l6o0l","Teachers/w0fu765wgnzvjjtjhfh5"]
        images_home = ["Home/gpfeadgzkbvpahexjzb7","Home/gpfeadgzkbvpahexjzb7","Home/omntzizohxvpewugguqs"]
        pw_hash = 'password'
        # num_professors = 10
        num_accepted_users = 15
        num_administrators= 0
        num_rejected_and_waiting_users = 5
        num_students_per_user = 2
        # num_classes_per_professor = 12
        pw_hash_user = 'password'

        classes_lower_years = ["Matematicas", "Lenguaje", "Ingles", "Artes", "Educacion Fisica", "Musica", "Religion"]
        classes_higher_years = ["Matematicas II", "Lenguaje II", "Ingles II", "Historia", "Ciencias", "Educacion Fisica", "Tecnologia", "Filosofia", "Computacion"]

        const_adm = Administrators(rut="9959656-2",password=pw_hash)
        const_adm.insert()

        const_user = Users(rut="152345256",name="Laura",lastname="Perez",password=pw_hash,status=1,email="example@gmail.com",phone_number="54526558")
        const_user.insert()
        const_student_1 = Students(rut="123456789",name="Tulio",lastname="Perez",school_year=5,parallel_name="A",attendance=0.9,status=1,user_rut=const_user.rut,email="example@gmail.com",phone_number="54236996")
        const_student_2 = Students(rut="123456780",name="Miguel",lastname="Perez",school_year=5,parallel_name="B",attendance=0.9,status=2,user_rut=const_user.rut,email="example@gmail.com",phone_number="54236996")
        const_student_1.insert()
        const_student_2.insert()

        for i in range(0, num_administrators):
            faker = Faker(
                    cls=Administrators,
                    init={
                        "rut": DemoSeeder.generate_random_rut(),
                        "password": pw_hash,
                    })
            for admn in faker.create(1):          
                admn.insert()
        for subject in classes_lower_years:
            faker = Faker(
                    cls=Professors,
                    init={
                        "rut": DemoSeeder.generate_random_rut(),
                        "name": generator.Name(),
                        "lastname": generator.Name(),
                        "phone_number": DemoSeeder.generate_random_phone(),
                        "email": generator.Email(),
                        "subject": subject,
                        "status": 1,
                    })
            for professor in faker.create(1):
                professor.insert()
                for i in range(1,9):
                    new_class = Classes(
                            subject=professor.subject,
                            school_year=i,
                            professor_rut=professor.rut,
                        )
                    new_class.insert()

        for subject in classes_higher_years:
            faker = Faker(
                    cls=Professors,
                    init={
                        "rut": DemoSeeder.generate_random_rut(),
                        "name": generator.Name(),
                        "lastname": generator.Name(),
                        "phone_number": DemoSeeder.generate_random_phone(),
                        "email": generator.Email(),
                        "subject": subject,
                        "status": 1,
                    })
            for professor in faker.create(1):
                professor.insert()
                for i in range(7,13):
                    new_class = Classes(
                            subject=professor.subject,
                            school_year=i,
                            professor_rut=professor.rut,
                        )
                    new_class.insert()

        for i in range(0, num_accepted_users):
            faker_accepted = Faker(
                    cls=Users,
                    init={
                        "rut": DemoSeeder.generate_random_rut(),
                        "name": generator.Name(),
                        "lastname": generator.Name(),
                        "password": pw_hash_user,
                        "status": 2,
                        "email": generator.Email(),
                        "phone_number": DemoSeeder.generate_random_phone(),
                    })
            for user in faker_accepted.create(1):
                    user.insert()

        for i in range(0, num_rejected_and_waiting_users):
            faker_rejected = Faker(
                cls=Users,
                init={
                    "rut":DemoSeeder.generate_random_rut(),
                    "name":generator.Name(),
                    "lastname":generator.Name(),
                    "password":pw_hash_user,
                    "status":0,
                    "email": generator.Email(),
                    "phone_number": DemoSeeder.generate_random_phone(),
                })
            faker_waiting =Faker(
                cls=Users,
                init={
                    "rut":DemoSeeder.generate_random_rut(),
                    "name":generator.Name(),
                    "lastname":generator.Name(),
                    "password":pw_hash_user,
                    "status":1,
                    "email": generator.Email(),
                    "phone_number": DemoSeeder.generate_random_phone(),
                })
            for user in faker_rejected.create(1):
                user.insert()
            for user in faker_waiting.create(1):
                user.insert()

        for user in Users.execute_all():
            for i in range(0,num_students_per_user):
                status = 0
                if user.status == 1:
                    status = 1
                elif user.status == 2:
                    status = 2
                
                faker = Faker(
                    cls=Students,
                    init={
                    "rut":DemoSeeder.generate_random_rut(),
                    "name":generator.Name(),
                    "lastname":generator.Name(),
                    "school_year":random.randint(1, 12),
                    "parallel_name":random.choice(["A", "B", "C"]),
                    "attendance":random.randint(70, 100)/100,
                    "status":status,
                    "user_rut":user.rut,
                    "email": generator.Email(),
                    "phone_number": DemoSeeder.generate_random_phone(),
                    }
                )
                for student in faker.create(1):
                    student.insert()

        for user in Users.execute_query_all():
             for student in Students.execute_query_all(user_rut=user.rut):
                adminitrator = random.choice(Administrators.execute_all())
                new_enrollment = EnrollmentApplications(
                    date=datetime.date.today(),
                    user_rut=user.rut,
                    student_rut=student.rut,
                    administrator_rut=adminitrator.rut,
                    status=student.status,
                )
                new_enrollment.insert()
        accepted_users = Users.execute_query_all(status=1)
        for professor in Professors.execute_all():
            
            new_appointment = Appointments(
                date=datetime.date.today(),
                user_rut=random.choice(accepted_users).rut,
                professor_rut=professor.rut,
            )
            new_appointment.insert()

        for student in Students.execute_query_all(status=1):
            classes= Classes.execute_query_all(school_year=student.school_year)
            for obj_class in classes:
                if obj_class.school_year == student.school_year:
                    new_class_student = ClassesStudents(
                        class_id=obj_class.id,
                        student_rut=student.rut,
                        grade=random.randint(40, 70),
                    )
                    new_class_student.insert()
        for url in images_about_us:
             new_image = Images(
                  name="",
                  description="About us image",
                  url=url
             )
             new_image.insert()
        
        for url in images_home:
            new_image = Images(
                  name="",
                  description= "Home image",
                  url=url
             )            
            new_image.insert()




# flask db downgrade
# flask db upgrade
# flask seed run

