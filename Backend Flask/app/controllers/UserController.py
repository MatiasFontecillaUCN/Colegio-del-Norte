from models.models import Users
from flask_bcrypt import Bcrypt
from flask import jsonify
from app.schemas.UsersSchema import UsersSchema
from Helpers.ValidationHelpers import ValidationHelpers

class UserController:

    def user_exists(rut, name, lastname, email, phone_number):
        rut = ValidationHelpers.validate_rut(rut)
        user = Users.execute_query(rut=rut)
        if user:
            if (user.name == name and
                user.lastname == lastname and
                user.email == email and
                user.phone_number == phone_number):
                return jsonify({"message":"Existe un usuario con esos datos","continue":True})
            return jsonify({"message":"Datos incorrectos","continue":False})
        return jsonify({"message":"No existe un usuario con esos datos","continue":True})    
    def validate_user(rut, name, lastname, email, phone_number):
        try:
            new_user = Users(
                password=rut,
                rut=rut,
                name=name,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
                status=2
            )
            return True
        except:
            return False
    def create_user(rut, name, lastname, email, phone_number):
        try:
            # rut = ValidationHelpers.validate_rut(rut)
            # email = ValidationHelpers.validate_email(email)
            # phone_number = ValidationHelpers.validate_phone_number(phone_number)
            # status = ValidationHelpers.validate_status(status)
            print(email)
            new_user = Users(
                password=rut,
                rut=rut,
                name=name,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
                status=2
            )
            new_user.insert()
            return True
        except Exception as e:
            print(e)
            return False


    def get_user(rut):
        rut = ValidationHelpers.validate_rut(rut)
        user = Users.execute_query(rut=rut)
        if(user):
            user_schema = UsersSchema()
            user_json = user_schema.dump(user)
            return jsonify(user_json)
        return jsonify({"message":"No existe ese usuario","exists":False})
    