from flask_restful import Resource
import requests
from dotenv import load_dotenv
from os import getenv

from models.Blog import Blog

class UpdateBlog(Resource):
    load_dotenv()
    medium_user = getenv('MEDIUM_USER')
    api_key = getenv('API_KEY')
    api_host = getenv('API_HOST')
    base_url = getenv('BASE_URL')

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host
    }

    def update(self):
        sqlite = Blog()
        sqlite.drop_table()
        sqlite.connect()

        data = self.get_resp(f'/user/id_for/{self.medium_user}')
        user_id = data.get('id')

        data = self.get_resp(f'/user/{user_id}/articles')
        article_ids = data.get('associated_articles')

        for article_id in article_ids:
            article = self.get_resp(f'/article/{article_id}')

            categories_string = ''
            for category in article.get('tags'):
                categories_string += f'{category},'
            
            description = ''
            description = article.get('subtitle')[22:102]
        
            sqlite_blog = Blog()
            sqlite_blog.connect()
            sqlite_blog.name = article.get('title')
            sqlite_blog.description = f'{description.capitalize()}...'
            sqlite_blog.link = article.get('url')
            sqlite_blog.categories = categories_string[:-1]
            sqlite_blog.save()

    def get_resp(self, endpoint):
        return requests.get(f'{self.base_url}{endpoint}', headers=self.headers).json()