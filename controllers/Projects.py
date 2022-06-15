from flask import jsonify
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Projects import Project

class Projects(Resource):
    load_dotenv()
    github_user = getenv('GITHUB_USER')

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