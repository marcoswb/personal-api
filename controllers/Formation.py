from flask_restful import Resource

class Formation(Resource):
    def get(self):
        return 'metodo get formation'