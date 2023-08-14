import requests
import os

from aws_lambda_update.classes.Posgres import Postgres

class UpdateProjects:
    github_user = os.environ['GITHUB_USER']

    def update(self):
        response = requests.get(f'https://api.github.com/users/{self.github_user}/repos')
        sqlite = Postgres()
        sqlite.clear
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