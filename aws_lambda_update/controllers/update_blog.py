import requests
import os

from aws_lambda_update.classes.Postgres import Postgres


class UpdateBlog:
    medium_user = os.environ['MEDIUM_USER']
    api_key = os.environ['API_KEY']
    api_host = os.environ['API_HOST']
    base_url = os.environ['BASE_URL']

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host
    }

    def update(self):
        postgres_db = Postgres()
        postgres_db.connect()
        postgres_db.clear_table('blog')

        data = self.get_resp(f'/user/id_for/{self.medium_user}')
        user_id = data.get('id')

        data = self.get_resp(f'/user/{user_id}/articles')
        article_ids = data.get('associated_articles')

        for article_id in article_ids:
            article = self.get_resp(f'/article/{article_id}')

            categories_string = ', '.join(article.get('tags'))
            description = f"{article.get('subtitle')[22:102]}..."

            postgres_db.insert_blog_post(article.get('title'), description.capitalize(), article.get('url'), categories_string)

        postgres_db.close_connection()

    def get_resp(self, endpoint):
        return requests.get(f'{self.base_url}{endpoint}', headers=self.headers).json()