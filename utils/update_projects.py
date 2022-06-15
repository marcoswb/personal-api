from flask_restful import Resource
import requests
from dotenv import load_dotenv
from os import getenv

from models.Projects import Project

class UpdateProjects(Resource):
    load_dotenv()
    github_user = getenv('GITHUB_USER')

    def update(self):
            response = requests.get(f'https://api.github.com/users/{self.github_user}/repos')
            sqlite = Project()
            sqlite.drop_table()
            sqlite.connect()

            for project in response.json():
                languages_response = requests.get(f"https://api.github.com/repos/{self.github_user}/{project['name']}/languages")

                languages_string = ''
                for language in languages_response.json():
                    languages_string += f'{language},'

                sqlite_project = Project()
                sqlite_project.connect()
                sqlite_project.name = project['name']
                sqlite_project.description = project['description']
                sqlite_project.link = project['html_url']
                sqlite_project.languages = languages_string[:-1]
                sqlite_project.save()