from flask import jsonify
from routes.ProfessorsRoutes import add_professor_routes
from routes.EnrollmentRoutes import add_enrollment_routes
from routes.StudentsRoutes import add_student_routes
from routes.UsersRoutes import add_user_routes
from routes.AuthRoutes import add_auth_routes
from routes.ImagesRoutes import add_images_routes



def add_routes(app):

    add_professor_routes(app)
    add_enrollment_routes(app)
    add_student_routes(app)
    add_user_routes(app)
    add_auth_routes(app)
    add_images_routes(app)

    @app.route('/', methods=["GET"])
    def healt_check():
        return jsonify({'msg': 'Server is healty'}), 200