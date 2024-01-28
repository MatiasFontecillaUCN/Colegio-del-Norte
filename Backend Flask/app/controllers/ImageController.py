from models.models import Images
from app.schemas.ImagesSchema import ImagesSchema
from flask import jsonify


class ImageController:

    def get_images():
        images = Images.execute_all()
        imagess_schema = ImagesSchema(many=True)
        images_json = imagess_schema.dump(images)
        return images_json
    
    def update_url(id, url):
        try:
            image = Images.execute_query(id=id)
            image.url = url
            image.update()
            return jsonify({'message': 'Imagen editada correctamente', 'url': image.url,'edited':True})
        except Exception as e:
            return jsonify({'message': 'Error al editar la imagen', 'Error': e,'edited':False})
