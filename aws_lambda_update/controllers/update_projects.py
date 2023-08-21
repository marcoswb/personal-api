import requests
import os

from aws_lambda_update.classes.Postgres import Postgres


class UpdateProjects:
    github_user = os.environ['GITHUB_USER']

    def update(self):
        response = requests.get(f'https://api.github.com/users/{self.github_user}/repos')
        postgres_db = Postgres()
        postgres_db.connect()
        postgres_db.clear_table()

        for project in response.json():
            languages_response = requests.get(f"https://api.github.com/repos/{self.github_user}/{project['name']}/languages")

            languages_string = ''
            for language in languages_response.json():
                languages_string += f'{language},'

            postgres_db.insert_project(project['name'], project['description'], project['html_url'], languages_string[:-1])

        postgres_db.close_connection()
