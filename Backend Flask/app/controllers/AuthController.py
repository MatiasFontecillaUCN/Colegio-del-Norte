from flask import jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from models.models import Users, Administrators
from Helpers.ValidationHelpers import ValidationHelpers

class AuthController:

    @staticmethod
    def login(rut, password):
        bcrypt = Bcrypt()
        rut = ValidationHelpers.validate_rut(rut)
        admin = Administrators.execute_query(rut=rut)
        user = Users.execute_query(rut=rut)
        try:
            if user:
                if(bcrypt.check_password_hash(user.password, password) and user.status == 1):
                    addtional_claims = {"roles":"user"}
                    access_token_user = create_access_token(identity=user.rut,additional_claims=addtional_claims)
                    return access_token_user
                elif(bcrypt.check_password_hash(user.password, password) and user.status == 2):
                    addtional_claims = {"roles":"temporal"}
                    access_token_temporal = create_access_token(identity=user.rut,additional_claims=addtional_claims)
                    return access_token_temporal
                
            elif admin:
                print(admin)
                if(admin and bcrypt.check_password_hash(admin.password, password)):
                    addtional_claims = {"roles":"admin"}
                    access_token_admin = create_access_token(identity=admin.rut,additional_claims=addtional_claims)
                    return access_token_admin
            return jsonify({'message': 'Invalid credentials'}), 401 
        except Exception as e:
            print(e)
            return jsonify({'message': e})