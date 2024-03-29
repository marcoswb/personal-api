from flask import request, Response, jsonify
from flask_restful import Resource
from dotenv import load_dotenv
from os import getenv

from models.Blog import Blog as ModelBlog


class Blog(Resource):

    @staticmethod
    def get():
        blog_db = ModelBlog()
        blog_db.connect()
        result = blog_db.select()
        blog_db.close_connection()

        blog_posts = []
        if result:
            for post in result:
                categories = post['categories'].split(',')

                blog_posts.append({
                    'name': post['name'],
                    'description': post['description'],
                    'link': post['link'],
                    'categories': categories
                })
        
        return jsonify(blog_posts)

    @staticmethod
    def post():
        load_dotenv()

        token = request.headers['Authorization']
        expected_token = getenv('TOKEN')
        if token == expected_token:
            args = request.json
            
            blog_db = ModelBlog()
            blog_db.connect()
            blog_db.clear_table()

            for item in args:
                data = {
                    'name': item['name'],
                    'description': item['description'],
                    'link': item['link'],
                    'categories': item['categories'],
                }
                
                blog_db.insert_line(data)
            blog_db.close_connection()
        else:
            return Response("{'status': 'Unauthorized'}", status=401, mimetype='application/json')
