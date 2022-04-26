from flask import jsonify
from flask_restful import Resource
import requests
from xml.etree import ElementTree
from dotenv import load_dotenv
from os import getenv

class Blog(Resource):
    load_dotenv()
    medium_user = getenv('MEDIUM_USER')

    def get(self):
        response = requests.get(f'https://medium.com/feed//@{self.medium_user}')
                    
        blog_posts = []
        posts = ElementTree.fromstring(response.content)[0]
        for post in posts.findall('item'):

            categories = []
            for category in post.findall('category'):
                categories.append(category.text)

            description = ''
            for elem in post.iter():
                if 'encoded' in elem.tag:
                    position_first_paragraph = (elem.text.find('<p>')+25)
                    description = elem.text[position_first_paragraph:position_first_paragraph+50]

            blog_posts.append({
                'name': post.find('title').text,
                'description': f'{description.capitalize()}...',
                'link': post.find('link').text,
                'categories': categories
            })
        
        return jsonify(blog_posts)