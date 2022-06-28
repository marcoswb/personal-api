from flask import request, Response, jsonify
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Projects import Project

class Projects(Resource):

    def get(self):
        try:
            sqlite = Project()
            sqlite.connect()

            projects = []
            data = sqlite.select().dicts()
            for project in data:
                languages = project['languages'].split(',')
                projects.append({
                    'name': project['name'],
                    'description': project['description'],
                    'link': project['link'],
                    'languages': languages
                })
                
            return jsonify(projects)
        except:
            return jsonify('Error in handle request.')

    def post(self):
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            print(args)
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')