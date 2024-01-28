
"""
Módulo init.py

Este módulo contiene las configuraciones y definiciones iniciales para la aplicación.

"""
import os
from flask import Flask, jsonify
from flask_seeder import FlaskSeeder
from database.db_mysql import db
from flask_bcrypt import Bcrypt
from routes.routes import add_routes
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from .ext import ma, migrate
from routes.routes import add_routes



def create_app():
    load_dotenv()
    app = Flask(__name__)
    db_username = os.getenv('db_username')
    db_password = os.getenv('db_password') 
    db_host = os.getenv('db_host')
    db_port = os.getenv('db_port')
    db_name = os.getenv('db_name')
    app.config['DEBUG'] = True
    app.config['FLASK_APP'] = os.getenv('FLASK_APP')
    app.config['FLASK_ENV'] = os.getenv('FLASK_ENV')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % (db_username, db_password, db_host,db_port, db_name)

    # Inicializa las extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    seeder = FlaskSeeder()
    seeder.init_app(app, db)
    ma.init_app(app)
    CORS(app)
    bcrypt = Bcrypt(app)
    add_routes(app)

    # Configuración de Flask-JWT-Extended
    app.config['JWT_SECRET_KEY'] = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
    jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = (
    '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc5'
    '12c15f69bb38307d11d5d17a41a7936789')

    return app