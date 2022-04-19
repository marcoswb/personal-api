from flask import jsonify
from flask_restful import Resource

from models.Projects import Projects as ModelProjects

class Projects(Resource):
    def get(self):
        database = ModelProjects()
        database.connect()
        result = database.select(
            ModelProjects.name,
            ModelProjects.description,
            ModelProjects.techs
        ).dicts()

        if result:
            projects = []
            for project in result:
                projects.append(project)
                
            return jsonify(projects)
        else:
            return jsonify([])