from flask import jsonify
from flask_restful import Resource
import requests
from dotenv import load_dotenv
from os import getenv

class Projects(Resource):
    load_dotenv()
    github_user = getenv('GITHUB_USER')

    def get(self):
        response = requests.get(f'https://api.github.com/users/{self.github_user}/repos')

        projects = []
        for project in response.json():
            languages_response = requests.get(f"https://api.github.com/repos/{self.github_user}/{project['name']}/languages")

            languages = []
            for language in languages_response.json():
                languages.append(language)

            projects.append({
                'name': project['name'],
                'description': project['description'],
                'html_url': project['html_url'],
                'languages': languages
            })
            
        return jsonify(projects)