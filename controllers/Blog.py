from flask import jsonify
from flask_restful import Resource
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