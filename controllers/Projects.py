from flask import request, Response, jsonify
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

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

    @staticmethod
    def post():
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            
            project_db = ModelProject()
            project_db.connect()
            project_db.clear_table()

            for item in args:
                data = {
                    'name': item['name'],
                    'description': item['description'],
                    'link': item['link'],
                    'languages': item['languages']
                }
                project_db.insert_line(data)
            project_db.close_connection()
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')
