from flask_restful import Resource

class Projects(Resource):
    def get(self):
        return 'metodo get projects'