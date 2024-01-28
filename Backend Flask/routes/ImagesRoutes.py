from flask import jsonify, request
from app.controllers.ImageController import ImageController
from flask_jwt_extended import jwt_required

def add_images_routes(app):

    @app.route("/image", methods=['GET','PATCH'])
    @jwt_required()
    def images():
        if request.method == 'GET':
            return ImageController.get_images()
        elif request.method == 'PATCH':
            data = request.get_json()
            return ImageController.update_url(data.get('id'),data.get('url'))