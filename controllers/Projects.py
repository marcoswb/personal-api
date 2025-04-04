from flask import jsonify
from flask_restful import Resource

from models.Projects import Project as ModelProject


class Projects(Resource):

    @staticmethod
    def get():
        project_db = ModelProject()
        project_db.connect()
        result = project_db.select_by_language()
        project_db.close_connection()

        projects = {}
        if result:
            for project in result:
                projects.setdefault(project.get('language'), [])

                projects[project.get('language')].append({
                    'id': project.get('id'),
                    'name': project['name'],
                    'description': project['description'],
                    'link': project['link'],
                    'languages': project['languages'].split(',')
                })

        return jsonify(projects)
