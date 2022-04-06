from flask_restful import Resource

class Blog(Resource):
    def get(self):
        return 'metodo get blog'