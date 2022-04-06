from flask_restful import Resource

class Experience(Resource):
    def get(self):
        return 'metodo get experience'