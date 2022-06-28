from flask import request, Response, jsonify
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Blog import Blog as BlogSQLite

class Blog(Resource):

    def get(self):
        sqlite = BlogSQLite()
        sqlite.connect()
        data = sqlite.select().dicts()

        blog_posts = []
        for post in data:
            categories = post['categories'].split(',')

            blog_posts.append({
                'name': post['name'],
                'description': post['description'],
                'link': post['link'],
                'categories': categories
            })
        
        return jsonify(blog_posts)

    def post(self):
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            print(args)
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')