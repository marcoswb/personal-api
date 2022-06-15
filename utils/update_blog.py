from flask_restful import Resource
import requests
from xml.etree import ElementTree
from dotenv import load_dotenv
from os import getenv

from models.Blog import Blog

class UpdateBlog(Resource):
    load_dotenv()
    medium_user = getenv('MEDIUM_USER')

    def update(self):
        response = requests.get(f'https://medium.com/feed//@{self.medium_user}')
        sqlite = Blog()
        sqlite.drop_table()
        sqlite.connect()
                    
        posts = ElementTree.fromstring(response.content)[0]
        for post in posts.findall('item'):

            categories_string = ''
            for category in post.findall('category'):
                categories_string += f'{category.text},'

            description = ''
            for elem in post.iter():
                if 'encoded' in elem.tag:
                    position_first_paragraph = (elem.text.find('<p>')+25)
                    description = elem.text[position_first_paragraph:position_first_paragraph+50]
            
            sqlite_blog = Blog()
            sqlite_blog.connect()
            sqlite_blog.name = post.find('title').text
            sqlite_blog.description = f'{description.capitalize()}...',
            sqlite_blog.link = post.find('link').text
            sqlite_blog.categories = categories_string[:-1]
            sqlite_blog.save()
