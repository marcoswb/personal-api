from flask import jsonify
from flask_restful import Resource

class Projects(Resource):
    def get(self):
        projects = []
            
        return jsonify(projects)