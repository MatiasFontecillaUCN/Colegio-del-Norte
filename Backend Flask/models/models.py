from database.db_mysql import db, BaseModelMixin
from sqlalchemy.orm import validates
from Helpers.ValidationHelpers import ValidationHelpers

# Models
class Administrators(db.Model, BaseModelMixin):
    __tablename__ = 'administrators'
    rut = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)    
    @validates('rut')
    def val_rut(self,key,value):
        return ValidationHelpers.validate_rut(value)
    @validates('password')
    def val_password(self,key,value):
        return ValidationHelpers.hash_password(value)

    def __init__(self, rut, password):
        self.rut = rut
        self.password = password
        return '<Administrators %r>' % self.rut
    
    def __repr__(self):
        return f"Administrator('{self.rut}')"
    
    def __str__(self):
        return f"Administrator('{self.rut}')" 
    
    def serialize(self):
        return{
            'rut': self.rut,
            'password':self.password,
        }
    def get_id(self):
        return self.rut
        
    
class Appointments(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    user_rut = db.Column(db.String(255), db.ForeignKey('users.rut'), nullable=False)
    professor_rut = db.Column(db.String(255), db.ForeignKey('professors.rut'), nullable=False)

    def __init__(self, date, user_rut, professor_rut):
        self.date = date
        self.user_rut = user_rut
        self.professor_rut = professor_rut
        return '<Appointments %r>' % self.id

    def __repr__(self):
        return f"Appointment('{self.id}')"
    
    def __str__(self):
        return f"Appointment('{self.date}, {self.user_rut}, {self.professor_rut}')"
       
class Classes(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(255), nullable=False)
    school_year = db.Column(db.Integer, nullable=False)
    professor_rut = db.Column(db.String(255), db.ForeignKey('professors.rut'))

    def __init__(self, subject, school_year, professor_rut):
        self.subject = subject
        self.school_year = school_year
        self.professor_rut = professor_rut
        return '<Classes %r>' % self.id
    
    def __repr__(self):
        return f"Class('{self.id}')"
    
    def __str__(self):
        return f"Class('{self.subject}, {self.school_year}')"
    
class ClassesStudents(db.Model, BaseModelMixin):
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), primary_key=True)
    student_rut = db.Column(db.String(255), db.ForeignKey('students.rut'), primary_key=True)
    grade = db.Column(db.Integer, nullable=False)

    def __init__(self, class_id, student_rut, grade):
        self.class_id = class_id
        self.student_rut = student_rut
        self.grade = grade
        return '<ClassesStudents %r>' % self.class_id
    
    def __repr__(self):
        return f"ClassesStudents('{self.class_id}, {self.student_rut}')"
    
    def __str__(self):
        return f"ClassesStudents('{self.class_id}, {self.student_rut}')"

class EnrollmentApplications(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    user_rut = db.Column(db.String(255), db.ForeignKey('users.rut'), nullable=False)
    student_rut = db.Column(db.String(255), db.ForeignKey('students.rut'), nullable=False)
    administrator_rut = db.Column(db.String(255), db.ForeignKey('administrators.rut'), nullable=False)

    def __init__(self, date, user_rut, student_rut, administrator_rut, status):
        self.date = date
        self.user_rut = user_rut
        self.status = status
        self.student_rut = student_rut
        self.administrator_rut = administrator_rut
        return '<EnrollmentApplications %r>' % self.id
    
    def __repr__(self):
        return f"EnrollmentApplication('{self.id}')"
    
    def __str__(self):
        return f"EnrollmentApplication('{self.date}, {self.user_rut}, {self.student_rut}')"

class Professors(db.Model, BaseModelMixin):
    rut = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer)
    
    @validates('rut')
    def val_rut(self,key,value):
        return ValidationHelpers.validate_rut(value)
    
    @validates('email')
    def val_email(self, key, value):
        return ValidationHelpers.validate_email(value)
    
    # @validates('phone_number')
    # def val_phone_number(self, key, value):
    #     return ValidationHelpers.validate_phone_number(value)
    
    def __init__(self, rut, name, lastname, phone_number, email, subject, status):
        self.rut = rut
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        self.email = email
        self.subject = subject
        self.status = status
        return '<Professors %r>' % self.name
    
    def __repr__(self):
        return f"Professor('{self.rut}')"
    
    def __str__(self):
        return f"Professor('{self.name}, {self.lastname}')"
    

class Students(db.Model, BaseModelMixin):
    rut = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    school_year = db.Column(db.Integer, nullable=False)
    parallel_name = db.Column(db.String(255), nullable=False)
    attendance = db.Column(db.Float, nullable=False)
    status = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    user_rut = db.Column(db.String(255), db.ForeignKey('users.rut'), nullable=False)

    @validates('rut')
    def val_rut(self,key,value):
        return ValidationHelpers.validate_rut(value)
    
    @validates('email')
    def val_email(self, key, value):
        return ValidationHelpers.validate_email(value)
    
    # @validates('phone_number')
    # def val_phone_number(self, key, value):
    #     return ValidationHelpers.validate_phone_number(value)

    def __init__(self, rut, name, lastname, school_year, parallel_name, attendance, status, user_rut, email, phone_number):
        self.rut = rut
        self.name = name
        self.lastname = lastname
        self.school_year = school_year
        self.parallel_name = parallel_name
        self.attendance = attendance
        self.status = status
        self.email = email
        self.phone_number = phone_number
        self.user_rut = user_rut
        return '<Students %r>' % self.name
    
    def __repr__(self):
        return f"Student('{self.rut}')"
    
    def __str__(self):
        return f"Student('{self.name}, {self.lastname}')"
    
class Users(db.Model, BaseModelMixin):
    rut = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)

    @validates('rut')
    def val_rut(self,key,value):
        return ValidationHelpers.validate_rut(value)
    
    @validates('email')
    def val_email(self, key, value):
        return ValidationHelpers.validate_email(value)
    
    # @validates('phone_number')
    # def val_phone_number(self, key, value):
    #     return ValidationHelpers.validate_phone_number(value)
    
    @validates('password')
    def val_password(self,key,value):
        return ValidationHelpers.hash_password(value)

    def __init__(self, rut, name, lastname, password, status, email, phone_number):
        self.rut = rut
        self.name = name
        self.lastname = lastname
        self.password = password
        self.status = status
        self.email = email
        self.phone_number = phone_number
        return '<Users %r>' % self.name
    
    def __repr__(self):
        return f"User('{self.rut}')"
    
    def __str__(self):
        return f"User('{self.name}, {self.lastname}')"
    
    def serialize(self):
        return{
            'rut': self.rut,
            'name':self.name,
            'lastname':self.lastname,
            'password':self.password,
            'status':self.status,
            'email':self.email,
            'phone_number':self.phone_number,
        }
    
class Images(db.Model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    url = db.Column(db.String(255), nullable=False)

    def __init__(self, name, description, url):
        self.name = name
        self.description = description
        self.url = url
        return '<Images %r>' % self.id

    def __repr__(self):
        return f"Images('{self.id}')"
    
    def __str__(self):
        return f"Images('{self.id}, {self.name}, {self.description}')"
